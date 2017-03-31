from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()


def draw_triangle(x, y, size):
    canvas.create_polygon(x, y+size, x-size, y-size*3**0.5/2, x+size, y-size*3**0.5/2, outline="black", fill="")
draw_triangle(300, 300, 300)

#draw_hexagon

def recursive_triangle(x, y, size):
    draw_triangle(x, y, size)
    if size > 5:
        recursive_triangle(x-size/2, y-size*3**0.5/4, size/2)
        recursive_triangle(x+size/2, y-size*3**0.5/4, size/2)
        recursive_triangle(x, y+size/2, size/2)


recursive_triangle(300, 300, 300)

root.mainloop()
