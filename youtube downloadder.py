import future
import tkinter
from tkinter import *
from pytube import *
from pytube import YouTube
from tkinter.filedialog import *
from tkinter import messagebox
import webbrowser
#from threading import *


video_size=0

def percentage(strem=None,chunk=None,file_handle=None,remaining=None):
    global video_size
    file_downloaded=(video_size-remaining)
    per=(file_downloaded/video_size)*100
    download_button.configure(text="{:00.0f} % Downloaded".format(per))

def thread():
    thread=Thread(target=startdownload)
    thread.start()

def startdownload():
    global video_size
    try:
            myurl=url_entry.get()
            download_button.configure(text="Please Wait..", )
            save_path = askdirectory()
            if save_path is None:
                return
            ob = YouTube(myurl, on_progress_callback = percentage)
            strem = ob.streams.first()
            video_size = strem.filesize
            strem.download(save_path)
            url_entry.delete(0, END)
            download_button.configure(text="Download")
            messagebox.askokcancel("downloaded", "File downloaded Successfully")

    except Exception as e:
        url_entry.delete(0,END)
        download_button.configure(text="Download")

def youtube_clicked():
    webbrowser.open("https://www.youtube.com")


#######Fornt END
root=tkinter.Tk()
root.configure(bg = "pink")
root.geometry("700x500+400+150")
root.resizable(0,0)
root.title("AB DOWNLOADER")
photo = tkinter.PhotoImage(file = 'download (1).png')
root.iconphoto(False,photo)

img=tkinter.PhotoImage(file="download_2_2.png")
image_label = tkinter.Label(root,bg="red",image=img)
image_label.pack()

label_url = tkinter.Label(root,text="Enter the url of vedio (copy and paste from youtube)",font=("Comic sans MS",10,"bold"))
label_url.pack(pady=(60,10))

label_urlhere = tkinter.Label(root,text="URL",font=(20),bg="red")
label_urlhere.pack(pady=(10,10))

url_entry=tkinter.Entry(root,width=40,font=("verdana",15),justify=CENTER,)
url_entry.pack(padx=10,fill=X)

download_button = tkinter.Button(root,bg="light green",text="Download Now",relief="ridge",font=("Comic sans MS",15,"bold"),width=15,command=thread)
download_button.pack(pady=(10,0))

image_youtube=tkinter.PhotoImage(file="h1.png")
check_youtube=Button(root,image=image_youtube,command=youtube_clicked,relief="ridge",text="Visit YouTube",font=("verdana",10,"bold"),bg="red",compound="right")
check_youtube.pack(padx=(400,0),pady=(50,0))

root.mainloop()


