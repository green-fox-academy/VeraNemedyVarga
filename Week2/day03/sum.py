# - Write a function called `sum` that sum all the numbers
#   until the given parameter
def sum(x):
    r = 0
    i = 1
    while i < x:
        r += i
        i += 1
    print(r)
