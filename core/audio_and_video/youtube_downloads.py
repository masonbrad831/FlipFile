from pytubefix import YouTube
from utils import utils
import os 


def download_mp3_from_youtube(url: str):
    try:
        yt = YouTube(url)

        audioStream = yt.streams.get_audio_only()

        if audioStream:
            outputFile = audioStream.download(utils.get_output_directory())
            print("\nDownload complete!")
            base, ext = os.path.splitext(outputFile)
            newFile = base + '.mp3'
            os.rename(outputFile, newFile)
        else:
            print("No suitable stream found.")
    except Exception as e:
        print("Failed to download")


def download_m4a_from_youtube(url: str):
    try:
        yt = YouTube(url)

        audioStream = yt.streams.get_audio_only()

        if audioStream:
            audioStream.download(utils.get_output_directory())
            print("\nDownload complete!")
        else:
            print("No suitable stream found.")
    except Exception as e:
        print("Failed to download")

def download_mp4_from_youtube(url: str):
    try:
        yt = YouTube(url)

        videoStream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if videoStream:
            print(utils.get_output_directory())
            videoStream.download(utils.get_output_directory())
            print("\nDownload complete!")
        else:
            print("No suitable stream found.")
    except Exception as e:
        print("Failed to download")
