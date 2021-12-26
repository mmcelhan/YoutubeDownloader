from pytube import YouTube
import os


def make_dir_if_not_exists(path):
    # makes directory if it doesn't exist
    os.makedirs(path, exist_ok=True)
    return None


def initialize():
    # initializes program by ensuring that download folder is created
    cur_work_dir = os.getcwd()
    dl_path = os.path.join(cur_work_dir, 'downloads')
    make_dir_if_not_exists(dl_path)
    return None


def file_scrub(text_input):
    # removes periods and commas from a file name
    text_input = text_input.replace(',', '').replace('.', '')
    return text_input


def youtube_dl(download_path, download_type='Video', link='https://www.youtube.com/watch?v=TK4N5W22Gts'):
    if download_type == 'Video':
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True).last()  # get highest resolution
        video.download(download_path)

    else:
        yt = YouTube(link)
        # gets the highest resolution audio but saves as a mp4
        audio = yt.streams.get_audio_only()
        audio.download(download_path)
        audio_root_name = yt.title

        # rename the file to mp3
        audio_file_name = str(file_scrub(audio_root_name)) + '.mp4'
        original_filename = os.path.join(download_path, audio_file_name)
        new_filename = os.path.join(download_path, audio_root_name + '.mp3')
        os.rename(original_filename, new_filename)

    return None  # end function
