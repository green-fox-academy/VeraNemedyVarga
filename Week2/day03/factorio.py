# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio(x):
    r = 1
    i = 1
    while i < x:
        r += r * i
        i += 1
    print(r)
factorio(4)
