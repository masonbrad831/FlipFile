from core.documents import docx_converter, pdf_converter
from core.audio_and_video import mp4_converter, youtube_downloads
from core.images import png_to_jpg
from utils import utils

def main():

    pdf_converter.convert_pdf_to_jpg("C:/Users/mason/Documents/GitHub/FlipFile/temp/file-sample_100kB.pdf")
    #mp4_converter.convert_mp4_to_mov("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_avi("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_ogv("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_webm("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")

    #mp4_converter.convert_mp4_to_mkv("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_wmv("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_mxf("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #mp4_converter.convert_mp4_to_m4v("C:/Users/mason/Documents/GitHub/FlipFile/temp/Project Hail Mary  Final Trailer.mp4")
    #youtube_downloads.download_mp4_from_youtube("https://www.youtube.com/watch?v=P0XN3-n-2Lo")
    #youtube_downloads.download_mp3_from_youtube("https://www.youtube.com/watch?v=P0XN3-n-2Lo")
    #youtube_downloads.download_m4a_from_youtube("https://www.youtube.com/watch?v=P0XN3-n-2Lo")
    #utils.delete_and_clear_temp_folder()

if __name__ == "__main__":
    main()