from utils import utils
from moviepy.video.io.VideoFileClip import VideoFileClip



def convert_mp4_to_mp3(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.audio.write_audiofile(str(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "mp3")))
        clip.close()
    except: 
        print("Failed to convert file!")

def convert_mp4_to_mov(filepath : str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "mov"), codec = 'libx264')
        clip.close()
        print("Success")
    except Exception as e:
        print(e) 

def convert_mp4_to_avi(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "avi"), codec = 'mpeg4')
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_webm(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "webm"), codec = 'libvpx')
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_ogv(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "ogv"), codec = 'libtheora')
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_mkv(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "mkv"), codec = 'libx264')
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_wmv(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "wmv"), codec = 'wmv2')
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_mxf(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "mxf"), 
                             codec = 'mpeg2video',
                             audio_codec = "pcm_s16le",
                             audio_fps = 48000,
                             bitrate = "50000k",
                             ffmpeg_params = ["-pix_fmt", "yuv422p"]
                             )
        clip.close()
        print("success")
    except Exception as e:
        print(e)

def convert_mp4_to_m4v(filepath: str):
    try:
        clip = VideoFileClip(filepath)
        clip.write_videofile(utils.get_output_directory_with_filename_and_ext(utils.get_filename_from_path(filepath), "m4v"), codec = 'libx264', audio_codec = "aac")
        clip.close()
        print("success")
    except Exception as e:
        print(e)