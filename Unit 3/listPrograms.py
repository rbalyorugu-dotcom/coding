foodlist = ["milk", "soda", "cookies", "chips"]

print(foodlist[0])
print(foodlist[3])

#replace an item with a new item at the
# previous index position

foodlist.pop("cookies")
foodlist.insert("apple")
print("milk","soda","apple","chips")

morningmenu = ["eggs and bacon", "pancakes","sausages and toast"]
afternoonmenu = ["hoagie","macoronni and cheese","salad"]
nightmenu = ["cheeseburger and fries","spagehtti","pizza"]

def restaurantmenu():
    print("Welcome." "What menu are you ordering from?")
    selection = input("Please select your menu depending on the time of day.")
    print("1." "morningmenu")
    print("2." "afternoonmenu")
    print("3." "nightmenu")
    if selection == 1:
        print("Whcih meal would you like?")
        print("1. eggs and bacon")
        print("2. pancakes")
        print("3. sausages and toast")
        meal = int(input())
        if meal == 1:
            print("Here are your eggs and bacon. Enjoy!")
        elif meal == 2:
            print("Here are your pancakes. Enjoy!")
        else meal == 3:
            print("Here are your sausages and toast")
        if meal == 
