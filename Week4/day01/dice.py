import random

class Dice():

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def getCurrent(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()

dice = Dice()

while dice.getCurrent() != [6, 6, 6, 6, 6, 6]:
    for i in range(len(dice.dice)):
        if dice.dice[i] != 6:
            dice.reroll(i)
            print(dice.dice)
print(dice.getCurrent())
