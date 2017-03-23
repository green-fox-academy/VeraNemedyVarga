# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 14, 16]
sublist = [4, 8, 12, 16]

def contains_all(sub, numlist):
    for i in sub:
        if i in numlist:
            x = "True"
        else:
            x = "False"
    return x
print(contains_all(sublist, listOfNumbers))

#if x in numbers:
#    print("Hoorray")
#    print("Nooo")
