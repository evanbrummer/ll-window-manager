from tkinter import *
from WinLinkedList import *

ll = WinLL()
sizing = False


def rmb_down(event):
    global ll, sizing
    sizing = True
    rectangle = canvas.create_rectangle(100, 50, 200, 100, fill="blue", tag="rect")

def rmb_move(event):
    head: Node = ll.head

    pass


# real stuff

root = Tk()
root.title = "winmgr"

canvas = Canvas(master=root, width=1280, height=720)
canvas.pack()

canvas.bind("<Button-3>", rmb_down) # create rectangle, start sizing
canvas.bind("<B3-Motion>", rmb_move) # resize head node rectangle


root.mainloop()