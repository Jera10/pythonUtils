import PyPDF2 as pdf
import os
import argparse

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Extract text from PDF files in a folder.")
parser.add_argument("source_folder", help="Path to the source folder containing PDF files")
parser.add_argument("target_folder", help="Path to the target folder to save text files")
args = parser.parse_args()

source_folder = args.source_folder
target_folder = args.target_folder

# Ensure the target folder exists
os.makedirs(target_folder, exist_ok=True)

# Iterate over all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(source_folder, filename)
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(target_folder, txt_filename)

        try:
            # Open the PDF file
            with open(pdf_path, 'rb') as file:
                reader = pdf.PdfReader(file)
                num_pages = len(reader.pages)

                # Extract text from each page
                extracted_text = ""
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    extracted_text += f"Page {page_num + 1}:\n{text}\n\n"

            # Save the extracted text to the results file
            with open(txt_path, 'w', encoding='utf-8') as results_file:
                results_file.write(extracted_text)

            print(f"Extracted text from '{filename}' has been saved to '{txt_filename}'")

        except FileNotFoundError:
            print(f"Error: The file '{pdf_path}' was not found.")
        except pdf.errors.PdfReadError:
            print(f"Error: The file '{pdf_path}' is not a valid PDF.")
