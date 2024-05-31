from tkinter import *
 
# root = Tk()
# root.title("winmgr")
 
# C = Canvas(root, bg="yellow", height=250, width=300) 

# line = C.create_line(108, 120, 320, 40, fill="green") 

# arc = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red") 

# oval = C.create_oval(80, 30, 140, 150, fill="blue")
 
# C.pack()
# mainloop()

def on_start(event):
  global rectangle, dragging, start_x, start_y
  dragging = True
  start_x = event.x
  start_y = event.y

def on_drag(event):
  global rectangle, dragging, start_x, start_y
  if not dragging:
    return
  x = event.x - start_x
  y = event.y - start_y
  canvas.move(rectangle, x, y)
  start_x = event.x
  start_y = event.y

def on_stop(event):
  global dragging
  dragging = False

# Create the main window
root = Tk()

# Set window title
root.title("winmgr")

# Create the canvas
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Create the rectangle object with a tag for easy manipulation
rectangle = canvas.create_rectangle(100, 50, 200, 100, fill="blue", tag="rect")

# Bind events to the canvas
canvas.bind("<Button-1>", on_start)  # Left mouse click starts dragging
canvas.bind("<B1-Motion>", on_drag)  # Left mouse click hold moves the rectangle
canvas.bind("<ButtonRelease-1>", on_stop)  # Left mouse click release stops dragging

# Global variables to track dragging state and starting position
dragging = False
start_x = None
start_y = None

# Run the main loop
root.mainloop()