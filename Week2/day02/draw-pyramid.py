# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
num = int(input('My man, gimme a number: '))
for i in range(1, num + 1):
    if int(num % 2 == 0):
        for j in range(0, (num // 2), -1):
            print(' ' * j, '*' * i)
    elif int(num % 2 == 1):
        for j in range(0, (num-1) // 2, -1):
            print(' ' * j, '*' * i)
