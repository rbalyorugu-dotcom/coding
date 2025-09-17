# How to create a function with data

# Step 1. Function definition
def bnbRefund(accountNumber, refundAmount):
    print('account number: ' + str(accountNumber))
    print('rfund amount: $'+ str(refundAmount) + 'to there account')

# Step 2. Function call (inovation)
bnbRefund(19292929, 3000)

def name_birthday (my_name, birth):
    print('my name is ' + my_name + 'my birthday is ' + birth)

name_birthday('robert', 'jan 3')

def dollarConverter(dollarAmount):
    pennies = dollarAmount * 100
    print('My '+ str(dollarAmount) + ' dollar(s) is equal to ' + str(pennies) + ' pennies.')
          
dollarConverter(5)










# area = length * width * Height



# Activity 3
# Create a function that will calculate the area of a triangle.
# Your function should take in 2 parameters. One will represent the length.
# and the other the width of the triangle.
# length = 20
# width = 15
# height = 23

def trianglearea(length, width, height):
    area = length * width * height
    print(area)

trianglearea(20, 15, 23, 6,900)




# Activity 4
# Create a temperature converter function to the changes.
# Fahrenheit to celsius. Your function should take in a
# parameter that will represent the temperature in fahrenheit you want to change.

# Convert fahrenheit to celsius using the following formula:

# Fahrenheit - int(32 * 5/9)


def temperatureCoverter(fahrenheit, celsius)
    celsius = fahrenheit - 32 * 5/9
    print('celsius' + 'is equal  to' 'fahrenheit' + int(32) * 5/9)