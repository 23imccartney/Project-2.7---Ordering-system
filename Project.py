import time, os

def main():
    """Home screen, gets a chocice of 1,2,3,4 from the user and catches errors"""
    while True:
        print(f"{'----- Sushi order -----':^13}\n{'1 Order    -    2 Menu':^13}\n{'3 About    -    4 Exit':^13}")
        choice = input("Enter an option: ").lower()
        if choice in ["1","2","3","4", "order", "menu", "about", "exit"]:
            return choice
        else:
            print("""Error, enter a number between 1 and 4
    e.g. 1
    not "five", -1 or 0""")
            time.sleep(1)
            os.system('cls')

def print_menu():
    print("Sushis:")
    for item, info in menu.items():
        if info["food_type"] == "sushi":
            print(item)


menu = {
"Salmon Nigiri" : {"price" : 3.50, "food_type" : "sushi"},

"Tuna Sashimi" : {"price" : 4.50, "food_type" : "sushi"},

"California Roll" : {"price" : 6.00, "food_type" : "sushi"},

"Spicy Tuna Roll" : {"price" : 6.50, "food_type" : "sushi"},

"Dragon Roll" : {"price" : 12.00, "food_type" : "sushi"},

"Cucumber Maki" : {"price" : 3.00, "food_type" : "sushi"},

"Teriyaki Chicken Bento" : {"price" : 14.50, "food_type" : "box"},

"Beef Yakiniku Bento" : {"price" : 16.00, "food_type" : "box"},

"Salmon Teriyaki Bento" : {"price" : 15.50, "food_type" : "box"},

"Vegetable Tempura Bento" : {"price" : 13.00, "food_type" : "box"},

"Chicken Yakisoba" : {"price" : 12.50, "food_type" : "noodles"},

"Shrimp Tempura Udon" : {"price" : 13.50, "food_type" : "noodles"},

"Tonkotsu Ramen" : {"price" : 14.00, "food_type" : "noodles"},

"Vegetable Yaki Udon" : {"price" : 11.50, "food_type" : "noodles"},

"Miso soup" : {"price" : 2.50, "food_type" : "drink"},

"Coca-cola" : {"price" : 3.00, "food_type" : "drink"},

"Sprite" : {"price" : 3.00, "food_type" : "drink"},

"Apple juice" : {"price" : 2.50, "food_type" : "drink"},
}

os.system('cls')

print_menu()

print()