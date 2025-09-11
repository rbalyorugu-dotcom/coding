# Functions - a function is a set of code instructions
# for a computer to follow.

# a function comes in 2 phrases
# Function Syntax (rules of how its written)
# functions have 2 phases

# phase 1: function definition
# we are describing the instructiion on what we want.
# this code to do. It only runs when we call it.
# 

def example():
    print('Good morning')

def example2():
    print('good day')
    a = input('enter a number: ')
    print(a)

# phase 2: function call/invocation
# when we are ready to use a function,
# we write it to use it.
example()
example2()

# we indent to inform the computer that we are about to write
# code instructions. If we don't, we will get an error.

def math():
    a = input('enter a number: ')
    b = 30
    print("Here i syour result! ")
    print(int(a)- + b)

#Create a function that calculate 2 unique user inputted numbers

def calculate():
    a = input('Please enter a number: ')
    b = input('Please enter another number: ')
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) / int(b))
    print(int(a) * int(b))

def calculate_custom():
    a = input(1,000)
    b= input(200)
    print(int(1,000) + (200))
    z = 1,200

calculate()