from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()


def draw_hexagon(x, y, size):
    canvas.create_polygon(x-size, y, x-size/2, y-size*3**0.5/2, x+size/2, y-size*3**0.5/2, x+size, y, x+size/2, y+size*3**0.5/2, x-size/2, y+size*3**0.5/2, fill='', outline="black")
#draw_hexagon(300, 300, 300)

#draw_hexagon

def recursive_hexagon(x, y, size):
    draw_hexagon(x, y, size)
    #time.sleep(0.1)
    #canvas.update()
    if size > 20:
        recursive_hexagon(x-size/4, y-size*3**0.5/4, size/2)
        recursive_hexagon(x+size/2, y, size/2)
        recursive_hexagon(x-size/4, y+size*3**0.5/4, size/2)


recursive_hexagon(300, 300, 300)

root.mainloop()
