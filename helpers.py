from pytubefix import YouTube
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


# little utility to parse out the resolution from a stream description like 1440p
def get_resolution(s):
    return int(s.resolution[:-1])




def file_scrub(text_input):
    # removes periods and commas from a file name
    text_input = text_input.replace(',', '').replace('.', '')
    return text_input


def youtube_dl(download_path, download_type='Video', link='https://www.youtube.com/watch?v=TK4N5W22Gts'):
    if download_type == 'Video':
        yt = YouTube(link)
        try:
            stream = max(
                filter(lambda s: get_resolution(s) <= 1080,  # filter out sub-1080p streams
                       filter(lambda s: s.type == 'video', yt.fmt_streams)),  # filter out the video streams
                key=get_resolution  # maximum resolution among those streams
            )

            stream.download(download_path)
        except:
            ys = yt.streams.get_highest_resolution()
            ys.download(download_path)

    else:
        yt = YouTube(link)
        # gets the highest resolution audio but saves as a mp4
        audio = yt.streams.get_audio_only()
        audio.download(download_path)
        audio_root_name = yt.title

        # rename the file to mp3
        original_filename = os.path.join(download_path, audio_root_name) + '.m4a'
        audio_file_name = os.path.join(download_path, str(file_scrub(audio_root_name))) + '.mp3'
        os.rename(original_filename, audio_file_name)

        """
        # rename the file to mp3
        audio_file_name = str(file_scrub(audio_root_name)) + '.m4a'
        original_filename = os.path.join(download_path, audio_file_name)
        new_filename = os.path.join(download_path, audio_root_name + '.mp3')
        os.rename(original_filename, new_filename)
        """
    return None  # end function
