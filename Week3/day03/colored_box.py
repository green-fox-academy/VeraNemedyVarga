from tkinter import *
root = Tk()

canvas = Canvas(root, width = "300", height = "300")
canvas.pack()

# draw a box that has different colored lines on each edge.
red_line = canvas.create_line(50, 50, 150, 50, fill = "red")
green_line = canvas.create_line(150, 50, 150, 150, fill = "green")
blue_line = canvas.create_line(50, 150, 150, 150, fill = "blue")
yellow = canvas.create_line(50, 50, 50, 150, fill = "yellow")

root.mainloop()
