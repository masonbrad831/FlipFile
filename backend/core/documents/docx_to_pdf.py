from pathlib import Path
import subprocess
from utils import utils


def convert_docx_to_pdf(docxFilePath):
    try:
        utils.libre_file_conversion_command("pdf", docxFilePath, utils.get_output_directory())
    except:
        print("Failed to convert file.")



