from pytube import YouTube
url = str(input())
path = str(input())
def download(url, path):
    try:
        yt = YouTube(url)
        yt.streams.first().download(path)
        return "Video in downloaded"
    except Exception:
        return "Error occurred"

print(download(url, path))
