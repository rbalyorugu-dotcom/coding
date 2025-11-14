# We can make it safer - Add authentication
# Add age limit to make 2 different variations based on age.
# optiion 1 - Add more ways to verify people.
# option 2 - Make a different version of tik-tok

 def signup():
        dob = input('what year were you born.'))
        tiktok_kids = []
        tiktok_teens = []
        tiktok_standard = []
        # 8 - 12 is kids
        # 13 - 18 is teen
        # 19 is adult
        currentYr = 2025
        usrAge = currentYr- dob
        print('my age is '+ str(usrAge))
        if usrAge > 8 and usrAge < 12:
            print('Welcome to tiktok kids')
            tiktok_kids.append(usrAge)
        elif usrAge > 12 and usrAge < 18:
            print('wasup chat, welcome to tik tok teens')
        else:
            print('welcome to the cesspool known as tik tok')
            tiktok_standard.append(usrAge)
signup()










# Use the SDLC steps we learned to build a simple calculator app.
# Step 1. ideation - what features should you have in your calculator app.
# Please write the 3 or 4 feeatures as strings
# examples
"Be able to do addition"
"Be able to subtract"
"Be able to find the square root"
"Be able to divide"

# Step 2. analysis and requirement - how would you code out your calculator
# please write atleast 1 function for 1 of your features


def calculator():
    numbers = input("input your numbers"))
    addition = []
    subtraction = []
    square root = []
    dividde = []
    print("Be able to do addition")
    