import tkinter
from tkinter.ttk import *
from PIL import ImageTk, Image
from pytube import YouTube

def Download():
    return 0
def Selection(text):
    youtube_video = YouTube(str(text))
    videolist = youtube_video.streams.filter(file_extension="mp4")
    combo = Combobox(middle_frame)
    combo['values'] = set(videolist)
    combo.current(2)
    combo.pack()


window = tkinter.Tk()
# This is the title for my window
window.title("YouTube Video Downloader By Joel Sathiyendra!")

# We create 2 frames to make the GUI look better
top_frame = tkinter.Frame(window,height=50).pack(fill="x")

label = tkinter.Label(window, text="Welcome to Joel's YouTube video downloader!", font=("Vineta BT", 16)).pack(fill="x")
bottom_frame = tkinter.Frame(window).pack(side="bottom", fill="x")

canvas = tkinter.Canvas(top_frame, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(r"C:\Users\MAC\Pictures\Saved Pictures\youtube1.png"))
canvas.create_image(150, 100, image=img)
middle_frame = tkinter.Frame(window, height=10).pack(fill="x")

url_label = tkinter.Label(middle_frame, text="Path").pack()
text = tkinter.Entry(middle_frame, width=30).pack()
button_select = tkinter.Button(middle_frame, text="Click me!", command=Selection).pack()

middle_frame2 = tkinter.Frame(window, height=20).pack()

button = tkinter.Button(bottom_frame, text="Download", height=1, width=40, bg="red", fg="Black", command=Download).pack()


window.geometry("800x600")
window.mainloop()
