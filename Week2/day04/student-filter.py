students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

def four_plus_candies(list_of_dictionaries):
    for dicto in students:
        if dicto["candies"] > 4:
            print(dicto["name"])

four_plus_candies(students)

def average_candies(list_of_dictionaries):
    summa = 0
    for dicto in students:
        summa += dicto["candies"]
    print(summa / len(students))

average_candies(students)
