from core.documents import pdf_to_docx, docx_to_pdf
from core.audio_and_video import mp4_to_mp3
from utils import utils

def main():
    pdf_to_docx.convert_pdf_to_word("C:/Users/mason/Downloads/drylab.pdf")
    docx_to_pdf.convert_docx_to_pdf("C:/Users/mason/Documents/GitHub/FlipFile/temp/drylab.docx")
    mp4_to_mp3.convert_mp4_to_mp3("C:/Users/mason/Downloads/mp4-test.mp4")
    utils.delete_and_clear_temp_folder()

if __name__ == "__main__":
    main()