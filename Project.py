import time, os

def main():
    """Home screen, gets a chocice of 1,2,3,4 from the user and catches errors"""
    while True:
        print(f"{'----- Sushi order -----':^13}\n{'1 Order    -    2 Menu':^13}\n{'3 About    -    4 Exit':^13}")
        choice = input("Enter an option: ").lower()
        if choice in ["1","2","3","4", "order", "menu", "about", "exit"]:
            return choice
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


def item_choice(given_list):
    """This function will get the users choices from the menu and store them, it will also add up the price"""
    while True:
        choice = input("Enter the item you would like to order (number or name):")
        if choice in menu or choice in ["1","2"]:
            print("pased")
        else:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")



menu = {
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

os.system('cls')


print_list(menu)
item_choice(menu)


print()