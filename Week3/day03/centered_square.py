from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.
line1 = canvas.create_line(145, 145, 155, 145, fill = "green")
line1 = canvas.create_line(155, 145, 155, 155, fill = "green")
line1 = canvas.create_line(145, 155, 155, 155, fill = "green")
line1 = canvas.create_line(145, 145, 145, 155, fill = "green")

root.mainloop()
