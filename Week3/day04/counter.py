
# Write a recursive function that takes one parameter: n and counts down from n.
def counter(n):
    if n == 0:
        return n
    else:
        return n + counter(n-1)

print(counter(5))
