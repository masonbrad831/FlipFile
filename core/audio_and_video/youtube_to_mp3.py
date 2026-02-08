from pytubefix import YouTube

def download_mp3_from_youtube(url: str, output: str):
    try:
        yt = YouTube(url)

        audioStream = yt.streams.get_audio_only()

        if audioStream:
            audioStream.download(output_path=output)
            print("\nDownload complete!")
        else:
            print("No suitable stream found.")
    except Exception as e:
        print("Failed to download")
