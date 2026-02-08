from pathlib import Path
import subprocess
import os

def get_filename_from_path(path):
    return Path((path.split("/"))[-1]).stem

def get_output_directory_with_filename_and_ext(fileName, ext):
    scriptDir = Path(__file__).parent
    outputDir = (scriptDir / "../temp").resolve()
    outputDir.mkdir(parents=True, exist_ok=True)
    return outputDir / f"{fileName}.{ext}"

def get_output_directory():
    scriptDir = Path(__file__).parent
    outputDir = (scriptDir / "../temp/").resolve()
    outputDir.mkdir(parents=True, exist_ok=True)
    print("OUTPUT DIR " + str(outputDir))
    return outputDir

def libre_file_conversion_command(fileType : str, fileDir, outputDir):
    subprocess.run([
        "soffice.exe", "--headless",
        "--convert-to", fileType,
        str(fileDir),
        "--outdir", str(outputDir)
        ], check=True)
    
def delete_and_clear_temp_folder():
    folder = get_output_directory()
    print(folder)
    for file in folder.iterdir():
        if file.is_file():
            try:
                file.unlink()
            except:
                    print("Failed")