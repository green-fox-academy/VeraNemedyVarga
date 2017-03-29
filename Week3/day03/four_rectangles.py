from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
square1 = canvas.create_rectangle(0, 0, 50, 50, fill = "green")
square1 = canvas.create_rectangle(150, 150, 230, 230, fill = "blue")
square1 = canvas.create_rectangle(150, 20, 210, 80, fill = "yellow")
square1 = canvas.create_rectangle(30, 120, 120, 210, fill = "black")


root.mainloop()
