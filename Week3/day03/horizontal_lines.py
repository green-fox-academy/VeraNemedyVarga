from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def line_draw(x, y):
    line = canvas.create_line(x, y, x + 50, y, fill = "green")

line_draw(0, 40)
line_draw(150, 70)
line_draw(200, 200)

root.mainloop()
