# De varios libros, artículos de investigación, etc. Hacer un buscador de información: pueden ser
# palabras o frases, donde se visualicen las páginas donde se encuentra la información y con
# posibilidad de consultar dichas páginas encontradas.

import fitz
import os
import sys
import re

def search_text(text, path):
    # Open the pdf file
    pdf_document = fitz.open(path)
    # Search the text in the pdf
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number] # Get the page
        text_instances = page.search_for(text) # Search the text in the page
        if len(text_instances) > 0: # If the text is found
            print(f"Text found in page {page_number + 1}") # Print the page number
            for text_instance in text_instances: # Print the text instances
                print(f"Text found at {text_instance}")
                # print all the pharagraph where the text is found
                x0 = text_instance[0]
                y0 = text_instance[1]
                x1 = text_instance[2]
                y1 = text_instance[3]
                width = x1 - x0
                height = y1 - y0
                x0 -= width + 100
                x1 += width + 100
                y0 -= height
                y1 += height
                text_instance = fitz.Rect(x0, y0, x1, y1)
                text_around = page.get_text("text", clip=text_instance)
                print(text_around)
                # open the pdf in the page where the text is found
                os.system(f"zathura {path} --page={page_number + 1}")

    # Close the pdf file
    pdf_document.close()

def main():
    # Get the path of the pdf file
    pdf_path = input("Enter the path of the pdf file: ")
    # Check if the path is valid
    if not os.path.exists(pdf_path):
        print("The path is not valid")
        sys.exit()
    # Get the text to search
    text = input("Enter the text to search: ")
    # Search the text in the pdf
    search_text(text, pdf_path)

if __name__ == "__main__":
    main()
