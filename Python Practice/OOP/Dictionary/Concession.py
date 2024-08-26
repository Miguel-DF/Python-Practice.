# Concession stand program

#data type of menu item
menu = {"pizza":3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries":2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda":3.00,
        "lemonade":4.25}
#data type for restore choice menu item
cart = []
# data type for total of choice menu item
total = 0
# print all menu items
print("----------MENU----------")
for key, value in  menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")

# while loop for choosing menu item and get quits if done choosing items
while True:
    food = input("Select an item(q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

#display of choosing item and compute it
print("---------Your Order---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

# print the total item choose
print()
print(f"Total is: ${total:.2f}'")