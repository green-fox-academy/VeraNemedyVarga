from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
width=300
height=300
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.

# create a loop that fills the canvas with rainbow colored squares.

rainbow=["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]


def square(size, color):
    squ = canvas.create_rectangle(width/2- size/2, height/2 - size/2, width/2 + size/2, height/2 + size/2, fill = color)

size = width

for i in range(0, len(rainbow)):
    color = rainbow[i]
    square(size, color)
    size -= width/(len(rainbow))


root.mainloop()
