import os
import sys
import win32com.client

def save_pdf_attachments(target_folder):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    account_name = "Name of the account"  # Replace with the actual account name
    parent_folder_name = "Name of the parent folder"  # Replace with the actual parent folder name"
    subfolder_name = "Name of the subfolder" # Replace with the actual subfolder name"

    # Find the correct account
    account = None
    for store in outlook.Folders:
        if store.Name == account_name:
            account = store
            break

    if not account:
        print(f"Account '{account_name}' not found.")
        return

    try:
        parent_folder = account.Folders[parent_folder_name]
        target_folder_obj = parent_folder.Folders[subfolder_name]
    except Exception as e:
        print(f"Folder path '{parent_folder_name} > {subfolder_name}' not found. Error: {e}")
        return

    messages = target_folder_obj.Items
    print(f"Found {len(messages)} messages in '{subfolder_name}'.")

    for message in messages:
        try:
            attachments = message.Attachments
            for attachment in attachments:
                if attachment.FileName.lower().endswith(".pdf"):
                    save_path = os.path.join(target_folder, attachment.FileName)
                    attachment.SaveAsFile(save_path)
                    print(f"Saved: {save_path}")
        except Exception as e:
            print(f"Error processing message: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python save_attachments.py <target_folder>")
        sys.exit(1)

    target_folder = sys.argv[1]
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    save_pdf_attachments(target_folder)

