# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
def bunny_ears(num):
    if num == 1:
        return 2
    elif num % 2 == 0:
        return 3 + bunny_ears(num-1)
    elif num % 2 != 0:
        return 2 + bunny_ears(num-1)

print(bunny_ears(200))
