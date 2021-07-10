from pytube import YouTube
url = 'link video youtube'
video = YouTube(url)
youtube = video.streams.get_highest_resolution()
youtube.download()

# diusahakan download ini --> pip install pytube di cmd setelah itu tulis source code di atas lalu jalankan kalau saya melalui cmd
# untuk youtube.download() --> itu digunakan untuk mengarahkan file ke mana alias buat video yang akan kita download disimpan di file mana karena 1 file jadi saya kosongkan.