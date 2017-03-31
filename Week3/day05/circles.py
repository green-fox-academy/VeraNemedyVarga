from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()


def draw_oval(x, y, size):
    canvas.create_oval(x-size, y-size, x+size, y+size, outline="black", fill="")
#draw_oval(300, 300, 300)

#draw_hexagon

def recursive_oval(x, y, size):
    draw_oval(x, y, size)
    if size > 5:
        recursive_oval(x, y-size/2, size/2)
        recursive_oval(x-size*0.43, y+size/4, size/2)
        recursive_oval(x+size*0.43, y+size/4, size/2)


recursive_oval(300, 300, 300)

root.mainloop()
