# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1,2,3,4,5,6,8];
x = 7

def elementfinder(num, list_of_num):
    if num in list_of_num:
        print("Hoorray")
    else:
        print("Nooo")

elementfinder(x, numbers)
