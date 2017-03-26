# - Create a variable named `ak` and assign the value `123` to it
# - Create a function called `doubling` that doubles it's input parameter
# - Print the result of `doubling(ak)`
ak = '123'
def doubling(word):
    return word * 2
print(doubling(ak))

def doubling_value(word):
    word = int(word) * 2
    return word
print(doubling_value(ak))
