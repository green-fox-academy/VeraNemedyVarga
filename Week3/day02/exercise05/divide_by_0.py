# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
#num = int(input("please enter a num: "))
def divide_by_zero():
    while True:
        try:
            num = int(input("Please enter a number: "))
            print(10/num)
            #break
        except ZeroDivisionError:
            print("Fail")
            #break
        finally:
            print("Loop complete")
divide_by_zero()
