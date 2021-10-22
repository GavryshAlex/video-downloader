from tkinter import *
from tkinter import messagebox
from pytube import YouTube
url = ""
path = ""
window = Tk()
window.title("YTD")
window.geometry("200x125")
window.resizable(0,0)
labelUrl = Label(text="Link")
entryUrl = Entry()
labelPath = Label(text="Path")
entryPath = Entry()
def download(url, path):
    yt = YouTube(url)
    yt.streams.first().download(path)
    messagebox.showinfo("Video is downloaded")
        #return "Video in downloaded"
    #except Exception:
     #   messagebox.showinfo("Error occurred")
        #return "Error occurred"
button = Button(text="Download", command = lambda: download(url, path))
labelUrl.pack()
entryUrl.pack()
labelPath.pack()
entryPath.pack()
button.pack()
while(True):
    url = entryUrl.get()
    path = entryPath.get()
    window.update()


window.mainloop()
