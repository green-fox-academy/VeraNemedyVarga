from tkinter import *

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
image_size = 72
#tkinter canvasen kívülre Label tkinter UI-jal kiírni a szöveges cuccokat, ami számontartja a levelt meg ilyesmit
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
                    self.draw_floor(x*image_size, y*image_size)
                else:
                    self.draw_wall(x*image_size, y*image_size)
        self.f.close()

    def area_indexing(self):
        self.f = open('game/area1.txt', 'r')
        self.f_read = self.f.readlines()
        self.tile_value_list = []
        for y in range(len(self.f_read)):
            for x in range(len(self.f_read[y])):
                self.tile_value_list.append(self.f_read[y][x])
                return self.tile_value_list

class GameObject(object):
    def __init__(self):
        pass
        # self.characterX
        # self.characterY

class Hero(GameObject):
    def __init__(self):
        super().__init__()
        self.character_down = PhotoImage(file="game/hero-down.png")
        self.character_up = PhotoImage(file="game/hero-up.png")
        self.character_left = PhotoImage(file="game/hero-left.png")
        self.character_right = PhotoImage(file="game/hero-right.png")
        self.character_images=[self.character_down, self.character_up, self.character_left, self.character_right]
        self.characterX = 0
        self.characterY = 0
        self.hero_image = 0

    def draw_hero(self):
        canvas.delete(self.hero_image)
        self.hero_image = canvas.create_image(self.characterX*image_size, self.characterY*image_size, anchor=NW, image = self.character_down)

    def on_key_press(self, e):
        self.e = e
        if self.e.keycode == 38:
            if self.characterY > 0:
                self.characterY = self.characterY-1
        elif self.e.keycode == 40:
            if self.characterY < 10:
                self.characterY = self.characterY+1
        elif self.e.keycode == 39:
            if self.characterX < 9:
                self.characterX = self.characterX+1
        elif self.e.keycode == 37:
            if self.characterX > 0:
             self.characterX = self.characterX-1
        self.draw_hero()

class Skeleton(GameObject):
    def __init__(self):
        self.skeleton = PhotoImage(file = "game/skeleton.png")
        self.characterX = 2
        self.characterY = 2
        self.skeleton_image = 0

    def draw_skeleton(self):
        canvas.delete(self.skeleton_image)
        self.skeleton_image = canvas.create_image(self.characterX * image_size, self.characterY * image_size, anchor = NW, image = self.skeleton)

    def on_key_press(self, e):
        self.e = e
        if self.e.keycode == 38:
            if self.characterY > 0:
                self.characterY = self.characterY-1
        elif self.e.keycode == 40:
            if self.characterY < 10:
                self.characterY = self.characterY+1
        elif self.e.keycode == 39:
            if self.characterX < 9:
                self.characterX = self.characterX+1
        elif self.e.keycode == 37:
            if self.characterX > 0:
             self.characterX = self.characterX-1
        self.draw_skeleton()



    # def move_hero(self):
    #     # self.on_key_press(self.e)
    #     # self.e = e
    #     area.area_indexing()
    #     if self.f_read[y][x] == 1:
    #         pass

area = Area()
area.draw_area()
gameobject= GameObject()
hero = Hero()
skeleton = Skeleton()
canvas.bind("<KeyPress>", hero.on_key_press)
canvas.focus_set()
skeleton.draw_skeleton()
hero.draw_hero()
#hero.move_hero()
root.mainloop()
