class Garden(object):
    def __init__(self):
        self.garden = []

    def add_plant(self, plant):
        self.garden.append(plant)


    def watering(self, water_amount):
        self.water_amount = water_amount


        if flower.current < 5:
            self.num_of_items.append(flower)
        if tree.current < 10:
            self.num_of_items.append(tree)

        for flower in self.num_of_items:
            flower.current += water_amount * len(num_of_items) * 0.75
        for tree in self.num_of_items:
            tree.current += water_amount * len(num_of_items) * 0.75



class Flower(object):
    def __init__(self, current, color):
        self.current = current
        self.color = color

        #def add_flower(self, flower)

class Tree(object):
    def __init__(self, current, color):
        self.current = current
        self.color = color


garden = Garden()
flower1 = Flower(3, "blue")
flower2 = Flower(2, "red")
flower3 = Flower(5, "green")
flower4 = Flower(4, "yellow")
#
#
garden.garden.append(flower1)
print(garden)
