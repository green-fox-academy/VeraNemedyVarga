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
                    print("The " + str(plant.color) + " Flower needs water." )
                    plant.current += spent_liters / self.counter * 0.75
                else:
                    print("The " + str(plant.color) + " Tree needs water." )
                    plant.current += spent_liters / self.counter * 0.4
            else:
                if plant.plant_type == "flower":
                    print("The " + str(plant.color) + " Flower doesn't need water." )
                else:
                    print("The " + str(plant.color) + " Tree doesn't need water." )

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

garden.watering_garden(0)
print('\n')
garden.watering_garden(40)
print('\n')
garden.watering_garden(70)
