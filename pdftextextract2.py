import os
import sys
import fitz  # PyMuPDF

def extract_text_from_pdfs(source_dir, destination_dir):
    # Ensure destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through all PDF files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(source_dir, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(destination_dir, txt_filename)

            try:
                doc = fitz.open(pdf_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                doc.close()

                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)
                print(f"Extracted text from {filename} to {txt_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_texts.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    extract_text_from_pdfs(source_directory, destination_directory)
