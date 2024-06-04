from tkinter import *
from WinLinkedList import *

ll = WinLL()
sizing = False


def rmb_down(event):
    global sizing, ll
    sizing = True
    n = Node(
        Rectangle(event.x, event.y, event.x, event.y)
    )
    nr = n.rect
    canvas.create_rectangle(nr.x0, nr.y0, nr.y1, nr.y1, fill="blue", tag="rect")
    ll.add_win(n)


def rmb_move(event):
    global sizing, ll
    if ll.head is None:
        return


def rmb_up(event):
    pass


def lmb_down(event):
    pass


def lmb_move(event):
    pass


def lmb_up(event):
    pass


def mmb_down(event):
    pass


# real stuff

root = Tk()
root.title = "winmgr"

canvas = Canvas(master=root, width=480, height=360)
canvas.pack()

canvas.bind("<Button-3>", rmb_down)  # create rectangle, start sizing
canvas.bind("<B3-Motion>", rmb_move)  # resize head node rectangle
canvas.bind("<ButtonRelease-3>", rmb_up)  # stop resizing, rectangle is locked in

canvas.bind("<Button-1>", lmb_down)  # move the highest intersecting node to the top, select for dragging
canvas.bind("<B1-Motion>", lmb_move)  # if head rect is selected, move it with the mouse
canvas.bind("<ButtonRelease-1>", lmb_up)  # stop moving with mouse and deselect

canvas.bind("<Button-2>", mmb_down)  # remove the highest intersecting rectangle

root.mainloop()
