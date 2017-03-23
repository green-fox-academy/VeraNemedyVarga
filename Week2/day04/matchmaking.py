# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve","Ashley","Bözsi","Kat","Jane"]
boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"]
order = []

#for i in range(len(girls)):
#    order.append(girls[i])
#for j in range(len(boys)):
#order.append(boys[j])
len(order) = len(girls) + len(boys)
for x in len(order):
    if x % 2 == 0:
        order.append(girls[x])

#order.append(x,y)
print(order)
