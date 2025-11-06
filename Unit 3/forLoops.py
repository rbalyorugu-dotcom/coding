#For Loops - A type of construct that runs code instructions
# A finite amount of times over a group of data.

halloweenCandy = ['snickers', 'starburst','m&ms','twizlers']

# for keyword - does all the loop work
# 'i' variable, the placeholder for the item in the group/list
# the 'i' variable can be named anything.
# 'i' is short for iterator.

for i in halloweenCandy:
    print(i)

numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    multi= i*3
    div= multi / 1.5
    print('These are the number multiplied by 3 and divided by 1/2: '+ str(div))


for i in range (0,5):
    print(i)


while range(0,50):
    print('x')


def tf():
    for x in range(3):
        print('true or false: 3 is greater than 2')
        answer = input()
        if answer != 'true':
            print('wrong, try again')
            print('attempt: '+ str(x))
        else:
            print('great')
            break


# Use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finished typing 5 words, 
# the for loop should end. 

# Clarification: program should ask the user to type in one word. Then the program
# should print it out and ask them to type another word. Your program
# should do this 5 times.

# Hint # 1: you should use the range() function.


# looping through stringgs
word = "Python"
for letter in word:
    print(letter)
    if letter == "p":
        print('did you mean paper? ')
    elif letter == 'y':
        print('did you mean python? ')






def words():
    for x in range(5):
        word = input("Please type in a word: ")
        print(word)
        if user = "1 word":
            print('attempt: '+ str(x))
        else:
            print('great')
            break





shoppingPrices = [3.00, 5.40, 7.20, 9.00]
total = 0
for items in shoppingPrices:
    total += items

print(total)



studentBody = ['a','b','c']
present = []
tardy = []
absent = []
for student in studentBody:
    # if scanned in add to present list
    # else add to absent list
    # absent.append(student)
    print('these students are present: ')
    print(present)
    print('these students are absent: ')
    print(absent)


# If you want to hack hypothetical attendence system to always be present
# if student.name == 'Ian Kimble':
# superhacking