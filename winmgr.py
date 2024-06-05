from tkinter import *
from WinLinkedList import *
import random

ll = WinLL()
intersecting = False


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))  # gpt 4-o is the goat


def rmb_down(event):
    global ll
    n = Node(
        Rectangle(event.x, event.y, event.x, event.y)
    )
    r = n.rect
    r.rid = canvas.create_rectangle(r.x0, r.y0, r.x1, r.y1, fill=random_color(), tag="rect")
    ll.add(n)


def rmb_move(event):
    global ll
    if ll.head is None:
        return

    r = ll.head.rect
    r.x1 = event.x
    r.y1 = event.y
    canvas.coords(r.rid, r.x0, r.y0, r.x1, r.y1)


def rmb_up(event):
    n = ll.head
    r = n.rect
    if r.x1 < r.x0:
        temp = r.x1
        r.x1 = r.x0
        r.x0 = temp

    if r.y1 < r.y0:
        temp = r.y1
        r.y1 = r.y0
        r.y0 = temp

    # lock it in, just in case user is doing something weird
    canvas.coords(r.rid, r.x0, r.y0, r.x1, r.y1)


def lmb_down(event):
    global ll, last_x, last_y, intersecting
    last_x = event.x
    last_y = event.y

    for n in ll:
        r = n.rect
        if r.intersects(event.x, event.y):
            intersecting = True
            ll.move_to_top(n)
            canvas.tag_raise(r.rid)
            break


def lmb_move(event):
    global ll, last_x, last_y, intersecting
    if intersecting is False:
        return
    if ll.head is None:
        return

    diff_x = event.x - last_x
    diff_y = event.y - last_y

    r = ll.head.rect
    r.x0 += diff_x
    r.x1 += diff_x
    r.y0 += diff_y
    r.y1 += diff_y
    canvas.coords(r.rid, r.x0, r.y0, r.x1, r.y1)

    last_x = event.x
    last_y = event.y


def lmb_up(event):
    global intersecting
    intersecting = False


def mmb_down(event):
    global ll

    for n in ll:
        r = n.rect
        if r.intersects(event.x, event.y):
            canvas.delete(r.rid)
            ll.remove(n)
            break

def full_remove(n: Node):
    canvas.delete(n.rect.rid)
    ll.remove(n)

def debug_nodes(event):
    count = 0
    for n in ll:
        count += 1

    print("there are", count, "nodes!")


# real stuff

root = Tk()
root.title("winmgr")

canvas = Canvas(master=root, width=1280, height=720)
canvas.pack()

canvas.bind("<Button-3>", rmb_down)  # create rectangle, start sizing
canvas.bind("<B3-Motion>", rmb_move)  # resize head node rectangle
canvas.bind("<ButtonRelease-3>", rmb_up)  # stop resizing, make sure it was created appropriately

canvas.bind("<Button-1>", lmb_down)  # move the highest intersecting node to the top, select for dragging
canvas.bind("<B1-Motion>", lmb_move)  # if head rect is selected, move it with the mouse
canvas.bind("<ButtonRelease-1>", lmb_up)  # stop moving with mouse and deselect

canvas.bind("<Button-2>", mmb_down)  # remove the highest intersecting rectangle

root.bind("n", debug_nodes)

root.mainloop()
