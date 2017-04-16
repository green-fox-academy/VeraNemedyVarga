class Garden(object):
    def __init__(self):
        self.flowers_and_trees = []

    def watering_garden(self, spent_liters):
        self.spent_liters = spent_liters
        self.counter = 0
        for plant in self.flowers_and_trees:
            self.counter += plant.needs_water()

        for plant in self.flowers_and_trees:
            if plant.needs_water() == 1:
                if plant.plant_type == "flower":
                    plant.current += spent_liters / self.counter * 0.75
                else:
                    plant.current += spent_liters / self.counter * 0.4

    def check_status(self):
        for plant in self.flowers_and_trees:
            pass


class Plant(object):
    def __init__(self, current, color, plant_type):
        self.current = current
        self.color = color
        self.plant_type = plant_type
        garden.flowers_and_trees.append(self)

    def needs_water(self):
        if (self.plant_type == "flower" and self.current < 5) or (self.plant_type == "tree" and self.current < 10):
            return 1
        else:
            return 0


garden = Garden()
flower1 = Plant(3, "blue", "flower")
flower2 = Plant(2, "yellow", "flower")
tree1 = Plant(4, "purple", "tree")
tree2 = Plant(11, "orange", "tree")
print(flower1.current, flower1.color)
print(garden.flowers_and_trees)
print(garden.flowers_and_trees[2].plant_type)
garden.watering_garden(7)
print(garden.flowers_and_trees[0].current)
print(garden.flowers_and_trees[1].current)
print(garden.flowers_and_trees[2].current)
print(garden.flowers_and_trees[3].current)
