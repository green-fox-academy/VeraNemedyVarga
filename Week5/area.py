from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
image_size = 72
# canvas.focus_set()
class Area(object):
    def __init__(self):
        self.floor = PhotoImage(file="game/floor.png")
        self.wall = PhotoImage(file="game/wall.png")
        self.board = [
            [0,0,0,1,0,1,0,0,0,0],
            [0,0,0,1,0,1,0,1,1,0],
            [0,1,1,1,0,1,0,1,1,0],
            [0,0,0,0,0,1,0,0,0,0],
            [1,1,1,1,0,1,1,1,1,0],
            [0,1,0,1,0,0,0,0,1,0],
            [0,1,0,1,0,1,1,0,1,0],
            [0,0,0,0,0,1,1,0,1,0],
            [0,1,1,1,0,0,0,0,1,0],
            [0,0,0,1,0,1,1,0,1,0],
            [0,1,0,1,0,1,0,0,0,0]
        ]

    def draw_floor(self, x, y):
        self.x = x
        self.y = y
        canvas.create_image(self.x, self.y, anchor=NW, image=self.floor)

    def draw_wall(self, x, y):
        self.x = x
        self.y = y
        canvas.create_image(self.x, self.y, anchor=NW, image = self.wall)

    def draw_area(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == 0:
                    self.draw_floor(x*image_size, y*image_size)
                else:
                    self.draw_wall(x*image_size, y*image_size)

    def get_position(self, x, y):
        if self.board[y][x] == 1:
            return False
        else:
            return True

class Hero(object):
    def __init__(self):
        self.hero_photo1 = PhotoImage(file = "game/hero-up.png")
        self.hero_photo2 = PhotoImage(file = "game/hero-down.png")
        self.hero_photo3 = PhotoImage(file = "game/hero-right.png")
        self.hero_photo4 = PhotoImage(file = "game/hero-left.png")
        self.hero_photo = self.hero_photo2
        self.characterX = 0
        self.characterY = 0
        self.hero_image = 0

    def draw_hero(self):
        canvas.delete(self.hero_image)
        self.hero_photo = self.hero_photo
        self.hero_image = canvas.create_image(self.characterX*image_size, self.characterY*image_size, anchor=NW, image = self.hero_photo)

    def move_hero(self, e):
        self.e = e

        if self.e.keycode == 38:
            if self.characterY > 0:
                if area.get_position(self.characterX, self.characterY-1) == True:
                    self.characterY = self.characterY - 1
                    self.hero_photo = self.hero_photo1

        elif self.e.keycode == 40:
            if self.characterY < 10:
                if area.get_position(self.characterX, self.characterY+1) == True:
                    self.characterY = self.characterY + 1
                    self.hero_photo = self.hero_photo2

        elif self.e.keycode == 39:
            if self.characterX < 9:
                if area.get_position(self.characterX+1, self.characterY) == True:
                    self.characterX = self.characterX + 1
                    self.hero_photo = self.hero_photo3

        elif self.e.keycode == 37:
            if self.characterX > 0:
                if area.get_position(self.characterX-1, self.characterY) == True:
                    self.characterX = self.characterX -1
                    self.hero_photo = self.hero_photo4

        self.draw_hero()

class Skeleton(object):
    def __init__(self):
        self.skeleton = PhotoImage(file = "game/skeleton.png")
        self.characterX = random.randint(0, 9)
        self.characterY = random.randint(0, 10)
        while area.get_position(self.characterX, self.characterY) == False:
            self.characterX = random.randint(0, 9)
            self.characterY = random.randint(0, 10)
        self.skeleton_image = 0

    def draw_skeleton(self):
        canvas.delete(self.skeleton_image)
        self.skeleton_image = canvas.create_image(self.characterX * image_size, self.characterY * image_size, anchor = NW, image = self.skeleton)



area = Area()
area.draw_area()
hero = Hero()
skeleton1 = Skeleton()
skeleton2 = Skeleton()
skeleton3 = Skeleton()

#canvas.bind("<KeyPress>", skeleton.move_skeleton)
canvas.bind("<KeyPress>", hero.move_hero)

canvas.focus_set()
hero.draw_hero()
skeleton1.draw_skeleton()
skeleton2.draw_skeleton()
skeleton3.draw_skeleton()



root.mainloop()
