from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]
x = 20
y = 20

for rect in range(20):
    canvas.create_rectangle(x, x, x+10, x+10, fill= "purple")
    x +=10

root.mainloop()
