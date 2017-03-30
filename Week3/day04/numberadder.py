# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def numberadder(n):
    if n == 1:
        return n
    else:
        return n + numberadder(n-1)

print(numberadder(6))
