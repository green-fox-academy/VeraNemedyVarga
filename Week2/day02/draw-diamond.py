# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#

num = int(input('My man, gimme a number: '))
for j, i in zip(range(2 * num - 1 , 0, -2), range(0, 2 * num, 2)):
    print(' ' * (i // 2) + '*' * j)
 list =
