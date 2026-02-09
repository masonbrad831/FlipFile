from pathlib import Path
from pdf2docx import Converter
from utils import utils
import pymupdf

def convert_pdf_to_docx(filepath: str):
    try:
        cv = Converter(filepath)
        cv.convert(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "docx"), start=0, end=None)
        cv.close()
    except Exception as e:
        print(e)

def convert_pdf_to_png(filepath: str):
    try:
        doc = pymupdf.open(filepath)
        
        folder_name = utils.get_filename_from_path(filepath)
        output_dir = Path(utils.get_output_directory()) / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        for i, page in enumerate(doc):
            file_path = output_dir / f"page_{i+1}.png"
            pix = page.get_pixmap(dpi=300)
            pix.save(str(file_path))
            
        doc.close()
        
    except Exception as e:
        print(e)

def convert_pdf_to_jpg(filepath: str):
    try:
        doc = pymupdf.open(filepath)
        
        folder_name = utils.get_filename_from_path(filepath)
        output_dir = Path(utils.get_output_directory()) / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        for i, page in enumerate(doc):
            file_path = output_dir / f"page_{i+1}.jpg"
            pix = page.get_pixmap(dpi=300)
            pix.save(str(file_path))
            
        doc.close()
        
    except Exception as e:
        print(e)

def convert_pdf_to_tiff(filepath : str):
    try:
        doc = pymupdf.open(filepath)
        pix = doc[0].get_pixmap(dpi=300)
        
    except Exception as e:
        print(e)

