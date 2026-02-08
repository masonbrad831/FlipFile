from pytubefix import YouTube

def download_mp4_from_youtube(url: str, output: str):
    try:
        yt = YouTube(url)

        videoStream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if videoStream:
            videoStream.download(output_path=output)
            print("\nDownload complete!")
        else:
            print("No suitable stream found.")
    except Exception as e:
        print("Failed to download")
