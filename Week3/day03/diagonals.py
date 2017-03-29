from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the canvas' diagonals in green.
left_diag = canvas.create_line(0, 0, 300, 300, fill = "green")
right_diag = canvas.create_line(300, 0, 0, 300, fill = "green")

root.mainloop()
