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
for i, j in zip(range(1, 2 * num + 1, 2), range(2 * num, 0, -2)):
    print(' ' * (j // 2) + '*' * i)
