import time, os, sys

def main():
    """Home screen, gets a chocice of 1,2,3,4 from the user and catches errors"""
    while True:
        os.system('cls')
        print(f"{'----- Koji Kitchen -----':^13}\n{'1 Order    -    2 Menu':^13}\n{'3 About    -    4 Exit':^13}")
        choice = input("Enter an option: ").lower()
        if choice in ["1", "2", "3", "4", "one", "two", "three", "four", "order", "menu", "about", "exit"]:
            if choice in ["order","1", "one"]:
                #order function
                finalise_order(*item_choice(menu))
                input("Press enter to continue:")
            elif choice in ["menu","2", "two"]:
                #menu
                print_list(menu)
                input("Press enter to continue:")
            elif choice in ["menu","2", "two"]:
                #about
                print("""Our Story
We opened Koji Kitchen back in 2018 with a pretty simple goal: to make really good Japanese food part of the local routine. People told us we were a bit brave opening a spot that focused on traditional Tonkotsu Ramen and hand-cut Sashimi in this neighborhood, but we figured that if we got the basics right, people would come.
Today, we’re mostly known for our signature Bento boxes and the "crazy" amount of effort we put into our Teriyaki Chicken. We still do things the long way—simmering our broths for hours and making sure every Dragon Roll is rolled to order. It’s fresh, it’s consistent, and it’s exactly the kind of food we love to eat ourselves.
Whether you're grabbing a quick Spicy Tuna Roll on your lunch break or sitting down for a big bowl of Yakisoba with the family, we’re just happy to be your local go-to.""")
                input("Press enter to continue:")
            else:
                #exit
                os.system('cls')
                sys.exit("Thank you!")


        else:
            print("""Error, enter a number between 1 and 4\ne.g. 1\nnot "five", -1 or 0""")
            time.sleep(1)
            os.system('cls')


def print_list(given_list):
    """this function prints the given list and sorts it into sushi, boxes, noodles and drinks, it also prints the index"""
    
    # print sushi
    print("Sushi:\n")
    for item, info in given_list.items():
        if info["food_type"] == "sushi":
            print(f"{info['position']}. {item}: {info['price']}$")

    # print bento boxes
    print("\n\nBento boxes:\n")
    for item, info in given_list.items():
        if info["food_type"] == "box":
            print(f"{info['position']}. {item}: {info['price']}$")

    # print noodles
    print("\n\nNoodles:\n")
    for item, info in given_list.items():
        if info["food_type"] == "noodles":
            print(f"{info['position']}. {item}: {info['price']}$")

    # print drinks
    print("\n\nDrinks:\n")
    for item, info in given_list.items():
        if info["food_type"] == "drink":
            print(f"{info['position']}. {item}: {info['price']}$")
    print("\n")


def find_choice(given_list, choice, key):
    """will fint the first key with the given varable e.g. will return "Salmon Nigiri" if "menu, 1, 'position'" given"""
    for item, info in given_list.items():
        if info.get(key) == choice:
            return item


def exit():
    exit = input('Press enter to continue, "finish" to continue to checkout\nor "cancel" to cancel order:\n').lower()
    if exit == "finish":
        return "break"
    elif exit == "cancel":
        os.system('cls')
        print("Cenceling order...")
        time.sleep(1.5)
        os.system('cls')
        main()


def item_choice(given_list):
    """This function will get the users choices from the menu and store them, it will also add up the price"""
    price = 0
    order = []
    while True:
        os.system('cls')
        print_list(menu)
        choice = input("Enter the item you would like to order (number or name):").capitalize()

        if choice in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]:
            choice = find_choice(menu, int(choice), "position")
            price += menu[choice]["price"]
            order.append(choice)
            print(f"Added {choice} - ${menu[choice]['price']} to order.\nTotal: ${price}")
            if exit() == "break":
                os.system('cls')
                print(f"Order:\n{order}\n\nTotal:\n${price}")
                return price,order

        elif choice in menu:
            price += menu[choice]["price"]
            order.append(choice)
            print(f"Added {choice} - ${menu[choice]['price']} to order.\nTotal: ${price}")
            if exit() == "break":
                os.system('cls')
                print(f"Order:\n{order}\n\nTotal:\n${price}")
                return price,order

        else:
            print("Could not find item.\nCheck capitals and spelling.\nYou can also use numbers to find items.")
            if exit() == "break":
                os.system('cls')
                print(f"Order:\n{order}\n\nTotal:\n${price}")
                return price,order
    

def get_int(txt):
    """Gets an integer and retuns it, will not except "five", 1.5 or -1 """
    while True:
        try:
            option = int(input(txt))
            if option <= 0:
                raise ValueError

        except ValueError:
            print("""Enter a positive number above zero \ne.g. 1\nNot "five", 1.5 or -1""")
            time.sleep(1)
            continue
        return option


def finalise_order(price, order):
    """will ask if person whants to pick up order or get it deliverd, will also calculate price"""
    while True:
        option = input(f"How would you like to get your food?:\n1. Pickup - no fee\n2. Delivery - {DELIVERY_PRICE_START} + ({DELIVERY_PRICE} perkm)\n").lower()
        if option in ["1","one","pickup"]:
            #pick up
            os.system('cls')
            print(f"Thank you for you order:\nOrder:\n{order}\n\nTotal:\n${price}")
            input("Press enter to continue:")
            main()
        elif option in ["2","two","delivery"]:
            #delivery
            while True:
                distance = get_int("Please enter how far away you are (km)")

                if distance > DELIVERY_MAX:
                    #distance validation:
                    option = input("We do not deliver that far\nPress enter to continue or Exit to chose a difrent option:")
                    if option == "exit":
                        break
                else:
                    os.system('cls')
                    print(f"Delivery will cost: ${DELIVERY_PRICE_START + (DELIVERY_PRICE*distance)}")
                    price += DELIVERY_PRICE_START + (DELIVERY_PRICE*distance)
                    print(f"Thank you for you order:\nOrder:\n{order}\n\nTotal:\n${price}")
                    input("Press enter to continue:")
                    main()
        else:
            input("Please enter 1,2,Pickup or delivery:\nPress enter to continue")
            continue



menu = {
"Nothing" : {"price" : 0.00, "food_type" : "sushi", "position" : 0},

"Salmon Nigiri" : {"price" : 3.50, "food_type" : "sushi", "position" : 1},

"Tuna Sashimi" : {"price" : 4.50, "food_type" : "sushi", "position" : 2},

"California Roll" : {"price" : 6.00, "food_type" : "sushi", "position" : 3},

"Spicy Tuna Roll" : {"price" : 6.50, "food_type" : "sushi", "position" : 4},

"Dragon Roll" : {"price" : 12.00, "food_type" : "sushi", "position" : 5},

"Cucumber Maki" : {"price" : 3.00, "food_type" : "sushi", "position" : 6},

"Teriyaki Chicken Bento" : {"price" : 14.50, "food_type" : "box", "position" : 7},

"Beef Yakiniku Bento" : {"price" : 16.00, "food_type" : "box", "position" : 8},

"Salmon Teriyaki Bento" : {"price" : 15.50, "food_type" : "box", "position" : 9},

"Vegetable Tempura Bento" : {"price" : 13.00, "food_type" : "box", "position" : 10},

"Custom box" : {"price" : "--", "food_type" : "box", "position" : 11},

"Chicken Yakisoba" : {"price" : 12.50, "food_type" : "noodles", "position" : 12},

"Shrimp Tempura Udon" : {"price" : 13.50, "food_type" : "noodles", "position" : 13},

"Tonkotsu Ramen" : {"price" : 14.00, "food_type" : "noodles", "position" : 14},

"Vegetable Yaki Udon" : {"price" : 11.50, "food_type" : "noodles", "position" : 15},

"Miso soup" : {"price" : 2.50, "food_type" : "drink", "position" : 16},

"Coca-cola" : {"price" : 3.00, "food_type" : "drink", "position" : 17},

"Sprite" : {"price" : 3.00, "food_type" : "drink", "position" : 18},

"Apple juice" : {"price" : 2.50, "food_type" : "drink", "position" : 19},
}

#delivery time per km in min
DELIVERY_TIME = 3
DELIVERY_Time_START = 5
#max delivery distance
DELIVERY_MAX = 150
#delivery price per km
DELIVERY_PRICE = 1.5
DELIVERY_PRICE_START = 5


os.system('cls')

main()

print()