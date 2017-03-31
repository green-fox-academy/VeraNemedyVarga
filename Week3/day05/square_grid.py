from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()

colors = ["red", "pink", "yellow", "blue", "black", "purple", "silver", "pink", "green"]
def draw_frame(x, y, size, yoyo):
    canvas.create_rectangle(x-size/2, y-size/2, x+size/2, y+size/2, fill=colors[int(yoyo/5)], width = yoyo, outline="red")

def recursive_frame(x, y, size, yoyo):
    draw_frame(x, y, size, yoyo)
    time.sleep(0.1)
    canvas.update()
    if yoyo > 5:
        recursive_frame(x-size/2, y-size/2, size/2, yoyo/2)
        recursive_frame(x-size/2, y+size/2, size/2, yoyo/2)
        recursive_frame(x+size/2, y+size/2, size/2, yoyo/2)
        recursive_frame(x+size/2, y-size/2, size/2, yoyo/2)


recursive_frame(300, 300, 300, 40)

root.mainloop()
