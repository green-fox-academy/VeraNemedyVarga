# Given a string, compute recursively a new string where all the 'x' chars have been removed.
def string_xremove(string):
    if len(string) == 0:
        return ""
    else:
        if string[0] == "x":
            return "" + string_xremove(string[1:])
        else:
            return string[0] + string_xremove(string[1:])

print(string_xremove("Vxerax"))
