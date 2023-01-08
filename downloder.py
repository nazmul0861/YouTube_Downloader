from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#Function
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()

    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloadig....')

    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selectry derectary
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File....')

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=700, height=700)
canvas.pack()

#logo
logo_img = PhotoImage(file='youtube.png')
#resize image
logo_img = logo_img.subsample(4, 4)
canvas.create_image(400, 80, image=logo_img)

#link Field

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download link: ", font={'Arial', 15})

#select path for saving the file
path_label = Label(screen, text="Select Path for Download", font={'Arial', 15})
select_btn = Button(screen, text="select", command=select_path)
#Add to Window

canvas.create_window(400, 350, window=path_label)
canvas.create_window(400, 450, window=select_btn)

#ad Widgets to window
canvas.create_window(400,270, window=link_label)
canvas.create_window(400, 320, window=link_field)

#download BTn

download_btn = Button(screen, text="Download File", command=download_file)
#Add to convas
canvas.create_window(400, 500, window=download_btn)

screen.mainloop()