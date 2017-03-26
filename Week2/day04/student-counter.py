students = [{'name': 'Teodor', 'age': 3, 'candies': 2}, {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints:
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies
def num_of_candies(list_of_dictionaries):
    candies_count = 0
    for dicto in list_of_dictionaries:
        candies_count += dicto["candies"]
    print(candies_count)

num_of_candies(students)

def agesum_5lass_candies(list_of_dictionaries):
    age = 0
    for dicto in list_of_dictionaries:
        if dicto["candies"] < 5:
            age += dicto['age']
    print(age)
agesum_5lass_candies(students)
