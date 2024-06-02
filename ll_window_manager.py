from tkinter import *


def lmb_down(event):
    global dragging, start_x, start_y
    if event.num == 1:  # Check for left click
        dragging = True
        start_x = event.x
        start_y = event.y
    elif event.num == 3:  # Check for right click
        create_new_rectangle(event.x, event.y)


def mouse_move(event):
    global dragging, start_x, start_y
    if not dragging:
        return
    x = event.x - start_x
    y = event.y - start_y
    canvas.move(rectangle, x, y)
    start_x = event.x
    start_y = event.y


def left_release(event):
    global dragging
    dragging = False


def create_new_rectangle(x, y):
    global rectangle
    new_rectangle = canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")  # Create new rectangle with offset
    # You can customize further: size, color based on preference
    rectangle = new_rectangle  # Update current rectangle for dragging


# Create the main window
root = Tk()

# Set window title
root.title("winmgr")

# Create the canvas
canvas = Canvas(root, width=1280, height=720)
canvas.pack()

# Initial rectangle
rectangle = canvas.create_rectangle(100, 50, 200, 100, fill="blue", tag="rect")

# Bind events to the canvas
canvas.bind("<Button-1>", lmb_down)  # Left click starts dragging
canvas.bind("<B1-Motion>", mouse_move)  # Left click hold moves the rectangle
canvas.bind("<ButtonRelease-1>", left_release)  # Left mouse click release stops dragging
canvas.bind("<Button-3>", lmb_down)  # Right click creates a new rectangle

# Global variables to track dragging state and starting position
dragging = False
start_x = None
start_y = None

# Run the main loop
root.mainloop()
