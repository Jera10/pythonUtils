# Installation:
# pip install docx2pdf

import os
import sys
from docx2pdf import convert

def convert_docx_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert all .docx files in the folder
    convert(input_folder, output_folder)
    print(f"Converted all .docx files from {input_folder} to {output_folder}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_docx_to_pdf.py <input_folder> <output_folder>")
        sys.exit(1)

    convert_docx_to_pdf(sys.argv[1], sys.argv[2])
