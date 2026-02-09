from pathlib import Path
from utils import utils
from docx import Document
import docx2txt
import mammoth
import pypandoc

def convert_docx_to_pdf(filepath: str):
    try:
        utils.libre_file_conversion_command("pdf", filepath, utils.get_output_directory())
    except:
        print("Failed to convert file.")
        
def convert_docx_to_txt(filepath: str):
    try:
        document_text = docx2txt.process(filepath)

        with open(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "txt"), "w", encoding="utf-8") as w:
            w.write(document_text)

    except Exception as e:
        print(e)

def convert_docx_to_rtf(filepath: str):
    try:
        pypandoc.convert_file(filepath, 'rtf', outputfile=utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "rtf"))
    except Exception as e:
        print(e)

def convert_docx_to_odt(filepath: str):
    try:
        #pypandoc.download_pandoc()
        pypandoc.convert_file(filepath, 'odt', outputfile=utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "odt"))
    except Exception as e:
        print(e)

def convert_docx_to_html(filepath: str):
    try:
        with open(filepath, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            complete_html = f"<!DOCTYPE html><html><body>{html}</body></html>"

            with open(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "html"), "w", encoding="utf-8") as w:
                w.write(complete_html)
    except Exception as e:
        print(e)



