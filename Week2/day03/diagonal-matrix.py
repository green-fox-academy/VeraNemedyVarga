# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1

ag = ["0", "0", "0", "0"]
for i in range (0, len(ag)):
    for j in range (0, len(ag)):
        if j == i:
            ag[i] = "1"
    print(str.join('\t', (ag)))
    ag = ["0", "0", "0", "0"]
