# create a python program can add to cart and compute the item you add in cart

# variable items
grocery = {"toothbursh": 1.00,
         "bath soap": 1.00,
         "collgate": 1.50,
         "shampoo": 0.50}
cart = [] # restore items
total = 0 # restore total of items

#display grocey items
print("--------SELECT ITEMS -----------")
for key, values in grocery.items():
    print(f"{key:10}: {values}")
print("--------------------------------")


# while loop for selecting items
while True:
    add = input("add to cart or (q if quit): ").lower()
    if add == "q":
        break
    elif grocery.get(add):
        cart.append(add)

#display the item choose
print("--------Your Cart -----------")
for add in cart:
    total += grocery.get(add)
    print(add, end= " ")

#dispaly the total of carts
print()
print(f"total of your cart is : {total}")

