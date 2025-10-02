# Nested Conditions = A conditional statement that has other conditional
# statements within it. Conditions inside of conditions.

def sandwichStore():
    print("welcome to Ian Foods. What would you like?")
    selection = input("Please select your main food item?")
    print("1. meatball sandwich")
    print("2. turkey sandwich")
    print("3. honey turkey sandwich")
    print("4. buffalo chicken sandwich")
    print("surprise me(mystery sandwich)")
    selection = input("Please select your main food item?")
    if selection == 1:
        print("you've selected the meatball sandwich")
        print("What sides do you want?")
        print("1. fries")
        print("2. salad")
        print("3. chips")
        side = int(input())
        if side == 1:
            print("great meatball and fries")
        elif side == 2:
            print("healthy! meatball and salad")
        elif side == 3:
            print("nice! meatball and chips")
        else:
            print("Sorry, don't understand your side.")
    if selection == 2:
        print("Sorry, we are out of the turkey sandwich.")
        sandwichStore()

sandwichStore()

def atm():
    balance = 5000
    pin = 1234
    
    userPin = int(input("please type in your bank pin number:"))
    if userPin == pin:
        print("welcome. What would you like to do?")
        print("1. withdraw money")
        print("2. deposit money")
        print("3. check your balance")
        selection = int(input())
        if selection == 1:
            amount = int(input("How much do you want to take out? "))
            if amount > balance:
                print("Sorry, you don't have that much in your account.")
        else:
            newBalance = balance- amount
            print("You are taking out: " + str(amount))
            print("Your new balance is:" +str(newBalance))
    elif selection == 2:
        print("How much would you like to deposit?")
        amount = int(input())
        newBalance = balance > amount
        print("you are adding: " + str(amount))
        print("your new balance is : " + str(newBalance))
    elif selection == 3:
        print("Your balance is: " + str(balance))
    else:
        print("Sorry incorrect.")
        atm()

atm()


# Python Lists = a way to organize data, regardless of data type.

# List Syntax- create a variable and then assign it to square brackets.
# write the data you want in your list in the square brackets.

groceries = ('words', 19, 12.3, True, 'new words')

print("1. Withdraw money")
print("2. Deposit money")
print("3. Check balance")

atmMenu = ("1. Withdraw money", 2. Deposit money, 3. Check balance")