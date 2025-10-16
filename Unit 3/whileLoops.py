# While Loop definition - a while loop is a type of construct
# where code instructions will keep on running so
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in your terminal, click crtl + c at the same time.

# While Loop Syntax

def ageCheck():
    ageToBuyGame = 17
    customerAge = int(input('how old are you: 15')

while ageToBuyGame >= customerAge:
    print("Sorry, you're not old enough to buy GTA VI.")
else:
    print("great, enjoy your collectors edition of GTA VI!")


savedPassword = '123Abc'
userPassword = input("please type in your password: ")

while savedPassword != userPassword:
    print("Incorrect try again please.")
    attempt += 1
    userPassword = input("Please type in your password again: ")
    if attempt == 3:
        print('Sorry, your account has been locked after 3 attempts. Please wait 5 minutes')
else:
    print