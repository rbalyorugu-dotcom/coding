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
    morningmenu = ["eggs and bacon", "pancakes","sausages and toast"]
    afternoonmenu = ["hoagie","macoronni and cheese","salad"]
    nightmenu = ["cheeseburger and fries","spagehtti","pizza"]

    print("Welcome." "What menu are you ordering from?")
    selection = input("Please select your menu depending on the time of day.")
    print("1." "morningmenu")
    print("2." "afternoonmenu")
    print("3." "nightmenu")
    if selection == morningmenu:
        print("It is breakfast")
        print("Which meal would you like?")
        print("1. eggs and bacon")
        print("2. pancakes")
        print("3. sausages and toast")
        meal = int(input())
        if meal == 1:
            print("Here are your eggs and bacon. Enjoy!")
        elif meal == 2:
            print("Here are your pancakes. Enjoy!")
        elif: meal == 3:
            print("Here are your sausages and toast")
        
    if selection == "afternoonmenu":
        print("It is lunch")
        print("Which meal would you like")
        print("1. hoagie.")
        print("2. macoronni and cheese.")
        print("3. salad")

        if meal == 1:
            print("Here is your hoagie. Enjoy!")
        elif meal == 2:
            print("Here is your macoronni and cheese. Enjoy!")
        elif meal == 3:
            print("Here is your salad. Enjoy!")
        else:
            print("Error; can't find that input.")

    if selection == "nightmenu":
        print("It is dinner")
        print("Which meal would you like?")
        print("1. cheeseburger and fries.")
        print("2.spaghetti")
        print("3. pizza")

        if meal == 1:
            print("Here are your cheesvurger and fries. Enjoy!")
        elif meal == 2:
            print("Here is your spaghetti. Enjoy!")
        elif meal == 3:
            print("Here is your pizza. Enjoy!")
        else:
            print("Error; can't find that input")

        restaurantmenu()