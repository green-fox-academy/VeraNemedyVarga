# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve","Ashley","Bözsi","Kat","Jane"]
boys = ["Joe","Fred","Béla","Todd","Neef", "Jeff"]
order = []

longer_list = max(len(girls), len(boys))
appendrest = boys if longer_list == len(boys) else girls
difference = (longer_list - min(len(girls), len(boys)))

for i, j in zip(range(0, len(girls)), range(0, len(boys))):
    order.append(girls[i])
    order.append(boys[j])
if difference != 0:
    order += (appendrest[-difference:])

print(order)
