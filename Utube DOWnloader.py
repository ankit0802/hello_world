from pytube import YouTube
from tkinter.filedialog import *

global_size=0
def startdownload():

    try:
        save_path = askdirectory()
        if save_path is None:
            return
        url = "https://www.youtube.com/watch?v=9HjgadGkkAo"
        ob = YouTube(url)
        strem = ob.streams.first()
        print((strem.filesize) / (1024 * 1024))
        print(strem.title)
        strem.download(save_path)
        print("done")
    except Exception as e:
        print(e)
        print("ERROR!!!")

startdownload()







