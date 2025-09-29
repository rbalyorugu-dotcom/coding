# Conditional statements = code that has a set of outcomes
# based on the data that is given.
# input--> condition --> output

# Conditional syntax = if / else
# If = the condition we are looking to satisfy

# Elif keyboard - same thing as the if keyboard

# Else = the default/ exit. The thing that happens
# When our condition is NOT satisfied.

def weather():
    weather = input("Whats the weather like today?")

    if weather == 'sunny':
        print("Its gonna be nice out. Wear shades.")

    elif (weather == 'rainy'):
        print("Bring a jacket.")
    elif (weather =='rainy'):
        print("Remember to bring an umbrella.")
    elif weather == 'chilly':
        print("Bring a jacket")
    else:
        print("Have a good day.")



def football():
    down = input('What down is it?')
    yards = input('How many yards do you need to get another first down?')

    if down == 1 and yards == 5:
        print("pass the ball!")
    elif down == 2 and yards < 8:
        print('short pass')
    elif down == 3 and yards < 6:
        print('run it')
    else: # this is the exit; assumes it is 4th down.
        print("punt")



# create a conditional block of code that acts as a
# password checker. The user should be able to input a
# password. If it is correct, they should get a message
# saying "welcome, you are logged in." Otherwise, they
# should get a message saying "try again."

def pw():
    password = input("Please enter your password")

    if password == 'sky':
        print("Welcome! You are logged in.")
    else:
        print('incorrect password')


# Create a function that will check whether a student is old
# enough to get there drivers permit. Your functions should accept
# 1 parameter. If the user is 16 and older, your function should
# return a message saying they can begin the process of getting
# their driver's permit. Otherwise, your function should
# inform the user they are not old enough

def student_age():
    if student_age >= 16:
        print('Congragulations, you can get your driver permit.')
    else:
        print("Sorry, you're not old enough yet.") 
    
student_age()

# Activity 2
# Create a function that will determine if a number is positive or negative.
# If a number is positive, it should print a message saying "this is positive."
# otherwise, the number must be negative

def numberCheck(number):
    if number == 'positive':
        print('This number is positive')
    else:
        print('This number is negative')

numberCheck()

# Activity 3
# Create a grade score checker function that allows a student to enter
# their numerical grade, and show them the letter grade. Your function
# should be able to process the grades as followed. If a grade number is
# below 70, it is an F. If a grade is above 70 and below 80, it is a C.
# if a grade is above 80 and below 90, it is a B.
# and lastly if a grade is above 90, its an A.

def gradeChecker(grade):
    if grade < 70:
        print('Your grade is a F')
    elif grade > 70 < 80:
        print('Your grade is a C')
    elif grade > 80 < 90:
        print('Your grade is a B')
    elif grade > 90:
        print('Your grade is an A')
    else grade = 100:

gradeChecker()