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
        self.f.close()

    def area_indexing(self):
        self.f = open('game/area1.txt', 'r')
        self.f_read = self.f.readlines()
        for y in range(len(self.f_read)):
            for x in range(len(self.f_read[y])):
                return self.f_read[y][x]

class Hero(object):
    def __init__(self):
        self.character = PhotoImage(file="game/hero-down.png")
        self.characterX = 0
        self.characterY = 0
        self.hero_image = 0

    def draw_hero(self, canvas):
        canvas.delete(self.hero_image)
        self.hero_image = canvas.create_image(self.characterX, self.characterY, anchor=NW, image = self.character)

    def on_key_press(self, e):
        self.e = self.e.keycode
        if self.e.keycode == 38:
            hero.characterY = hero.characterY - 72
        elif self.e.keycode == 40:
            hero.characterY = hero.characterY + 72
        elif self.e.keycode == 39:
            hero.characterX = hero.characterX + 72
        elif self.e.keycode == 37:
            hero.characterX = hero.characterX -72

        #hero.draw_hero(canvas)

area = Area()
area.draw_area()
hero = Hero()
canvas.bind("<KeyPress>", hero.on_key_press)
canvas.focus_set()

hero.draw_hero(canvas)
root.mainloop()
