import sys
import os
import fitz  # PyMuPDF

def merge_pdfs(input_folder, output_path):
    merged_pdf = fitz.open()

    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            pdf_document = fitz.open(pdf_path)
            merged_pdf.insert_pdf(pdf_document)

    merged_pdf.save(output_path)
    print(f"Merged PDF saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <input_folder> <output_path>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_path = sys.argv[2]

    merge_pdfs(input_folder, output_path)
