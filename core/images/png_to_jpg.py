from pathlib import Path
from utils import utils
from PIL import Image

def convert_png_to_jpg(filepath):
    try:
        with Image.open(filepath) as image:
            rgb_image = image.convert('RGB')
            rgb_image.save(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "jpg"), 'jpeg')
    except:
        print("Failed to convert png file")