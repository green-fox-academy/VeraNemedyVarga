shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
shop_items[-1] = "Ice Cream"
shop_items[1] = "Croissant"
print(shop_items)
