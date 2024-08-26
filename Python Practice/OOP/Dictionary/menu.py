# create a function python program can view item, add to cart and purchase

#function for view menu
def menu():
    menus = {"Pizza": 2.5,
             "Coke": 1.0,
             "Donut": 2.5,
             "Pretzel": 1.5}
    cart = []
    total = 0

    #display menu
    print("--------SELECT ITEMS -----------")
    for key, value in menus.items():
        print(f"{key:10} : {value:.2f}")
    print("--------------------------------")

def system_display():
    print("Input Start")
    choose = input("Start or Exit : ").lower()

    if choose == "Start":
        menu()
    elif choose == "Exit":
        print("Ordering End")

system_display()

