# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
"""for i in range(1, 5):"""
i1 = int(input('Please type an integer: '))
i2 = int(input('Please type a second integer: '))
i3 = int(input('Please type a third integer: '))
i4 = int(input('Please type a fourth integer: '))
i5 = int(input('Please type a fifth and last integer: '))
szum = (i1 + i2 + i3 + i4 + i5)
noOfis = 5

print('Sum: ' + str(szum))
print('Average: ' + str(szum / 5))
