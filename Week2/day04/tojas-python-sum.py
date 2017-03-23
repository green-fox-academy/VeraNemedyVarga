number = 5
out = 0     #ha az out a for-on belül lenne, minden új loop elején lenullázná az outot újra és újra
for i in range(1, number + 1):
    out += 1

print(out)  #változó

#pakoljuk bele a fentit egy functionbe
number = 5      #lévén hogy a változó a függvényen kívül van, ezért nem tudom később változtatni
def sum(n):     #az n itt sokkal rugalmasabb, lokális változó, amit később variálhatunk
    out = 0
    for i in range(1, n + 1):
        out += 1
    return out      #a return azért fasza mert később még fel tudom használni - nem úgy a printtel

print(sum(number))
