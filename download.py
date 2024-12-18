from pytube import YouTube
from pytubefix import YouTube

url = 'link video youtube'

downloads_folder = r"C:\Users\HP\Downloads"

video = YouTube(url)
youtube = video.streams.get_highest_resolution()
# youtube = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

youtube.download(output_path=downloads_folder)
