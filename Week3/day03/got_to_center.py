from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.


def line_draw(x, y):
    line = canvas.create_line(x, y, 150, 150, fill = "blue")

line_draw(0, 0)
line_draw(0, 70)
line_draw(60, 80)
root.mainloop()
