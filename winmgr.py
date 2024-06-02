from tkinter import *
from WinLinkedList import WinLL

ll = WinLL()
sizing = False


def rmb_down(event):
    global ll, sizing
    sizing = True
    rectangle = canvas.create_rectangle(100, 50, 200, 100, fill="blue", tag="rect")


# real stuff

root = Tk()
root.title = "winmgr"

canvas = Canvas(master=root, width=1280, height=720)
canvas.pack()

canvas.bind(sequence="<Button-3>", func=rmb_down)

root.mainloop()