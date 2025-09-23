# Conditional statements = code that has a set of outcomes
# based on the data that is given.

# Conditional syntax = if / else
# If = the condition we are looking to satisfy
# Else = the default/ exit. The thing that happens
# When our condition is NOT satisfied.
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
# create a conditional block of code that acts as a
# password checker. The user should be able to input a
# password. If it is correct, they should get a message
# saying "welcome, you are logged in." Otherwise, they
# should get a message saying "try again."

password = input("Please enter your password")

if password == 'sky':
    print("Welcome! You are logged in.")
else:
    print('incorrect password')