from utils import utils
from moviepy.video.io.VideoFileClip import VideoFileClip


def convert_mp4_to_mp3(mp4Path):
    try:
        clip = VideoFileClip(str(mp4Path))
        clip.audio.write_audiofile(str(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(mp4Path), "mp3")))
        clip.close()
    except: 
        print("Failed to convert file!")