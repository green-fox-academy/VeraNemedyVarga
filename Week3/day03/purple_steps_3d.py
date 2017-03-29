from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]
x = 10
y = 20
for rect in range(6):
    rect = canvas.create_rectangle(x, x, y, y, fill= "purple")
    x = y
    y *= 1.5
root.mainloop()
