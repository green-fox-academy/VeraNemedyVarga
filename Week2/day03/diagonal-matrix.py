# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
#[1, 0, 0, 0]
#[0, 1, 0, 0]
#

ag = [0, 0, 0, 0]
for i, j in zip(range(0, len(ag)), range(0, len(ag))):
    if j == i:
        ag[i] = 1
    else:
        ag[i] = 0
    print(ag)
