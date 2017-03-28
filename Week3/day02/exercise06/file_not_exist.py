# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.
filename = input("Enter file name": )
askforfile = open(filename, "r")
read_content = askforfile.readlines()
print(len(read_content))
