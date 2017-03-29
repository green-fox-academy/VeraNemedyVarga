from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
width = 300
height = 300
x = 0
y = 0
def draw_to_center(x, y):
    for y in range(0, width +20, 20):
        canvas.create_line(0, y, width/2, height/2)
    for y in range(0, width + 20, 20):
        canvas.create_line(width, y, width/2, height/2)
    for x in range(0, height+20, 20):
        canvas.create_line(x, 0, width/2, height/2)
    for x in range(0, height+20, 20):
        canvas.create_line(x, width, width/2, height/2)
draw_to_center(0, 0)


root.mainloop()
