pirate = {"name" : "Jack", "gold" : 7, "has_wooden_leg" : True}
#A dictionary key-jeit is strignbe kell rakni.
print(pirate["name"])
pirate["gold"] = 8      #felülírja a "gold" értékét. A kulcsokkal tudom elkérni az értékeket.
print(pirate["gold"])

for key in pirate:
    print(key)
    print(pirate[key])

for key, value in pirate.items():
    #print(key + " : " + str(value))
    print(key)
    print(value)
