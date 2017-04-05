# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    return max(a, b, c)

# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    if len(pool) % 2 == 0:
        index1 = int(len(pool)/2 - 1)
        index2 = int(len(pool)/2)
        median = (pool[index1] + pool[index2])/2
        return median
    else:
        index = int(len(pool)/2)
        return pool[index]
# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aäeiouúéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve

# Run the tests, all 10 should be green (passing).
# The implementations though are not quite good.
# Create tests that'll fail, and will show how the implementations are wrong
# After creating the tests, fix the implementations
# Check again, if you can create failing tests
# Implement if needed
