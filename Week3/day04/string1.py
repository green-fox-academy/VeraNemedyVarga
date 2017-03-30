# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
"""def string_xtoy(string):
    if 'x' not in string:
        return string
    else:
        return string.replace('x', 'y')

print(string_xtoy("Veraxx"))"""

def string_xtoy(string):
    if len(string) == 0:
        return ""
    else:
        if string[0] == "x":
            return "y" + string_xtoy(string[1:])
        else:
            return string[0] + string_xtoy(string[1:])


print(string_xtoy("Vera"))
