from pathlib import Path
from pdf2docx import Converter
from utils import utils

def convert_pdf_to_word(pdfFilePath):
    try:
        cv = Converter(pdfFilePath)
        cv.convert(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(pdfFilePath), "docx"), start=0, end=None)
        cv.close()
    except:
        print("Failed to convert PDF file")