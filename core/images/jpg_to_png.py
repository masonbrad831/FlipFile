from pathlib import Path
from utils import utils
from PIL import Image

def convert_jpg_to_png(filepath):
    try:
        with Image.open(filepath) as image:
            image.save(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "png"), 'PNG')
    except:
        print("Failed to convert png file")
    