from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
width = 300
height = 300

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
def square(x):
    sq = canvas.create_rectangle(width/2 - x/2, height/2 - x/2, width/2 + x/2, height/2 + x/2, fill = "blue")

square(50)
square(90)
square(120)

root.mainloop()
