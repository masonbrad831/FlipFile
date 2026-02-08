from pathlib import Path
import subprocess



def convert_docx_to_pdf(docxFilePath):
    #Grab the file name
    fileName = Path((docxFilePath.split("/"))[-1]).stem
    print(fileName)

    #get temp folder location
    scriptDir = Path(__file__).parent
    outputDir = (scriptDir / "../../temp").resolve()
    outputDir.mkdir(parents=True, exist_ok=True)
    completePdfFilePath = outputDir / f"{fileName}.pdf"
    print(completePdfFilePath)

    try:
        subprocess.run([
        "soffice.exe", "--headless",
        "--convert-to", "pdf",
        str(docxFilePath),
        "--outdir", str(Path(completePdfFilePath).parent)
        ], check=True)
    except:
        print("Failed to convert file.")
    



