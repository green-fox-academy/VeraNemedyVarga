from tkinter import *

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
# canvas.focus_set()
class Area(object):
    def __init__(self):
        self.floor = PhotoImage(file="game/floor.png")
        self.wall = PhotoImage(file="game/wall.png")

    def draw_floor(self, x, y):
        self.x = x
        self.y = y
        canvas.create_image(x, y, anchor=NW, image=self.floor)

    def draw_wall(self, x, y):
        self.x = x
        self.y = y
        canvas.create_image(x, y, anchor=NW, image = self.wall)

    def draw_area(self):
        self.f = open('game/area1.txt', 'r')
        self.f_read = self.f.readlines()
        self.image = PhotoImage(file = 'game/floor.png')
        for y in range(len(self.f_read)):
            for x in range(len(self.f_read[y])):
                if self.f_read[y][x] == "0":
                    self.draw_floor(x*72, y*72)
                else:
                    self.draw_wall(x*72, y*72)


area = Area()
area.draw_area()
root.mainloop()
