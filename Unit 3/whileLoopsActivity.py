def numberLoop():
    userNumber = input("Enter a list of numbers: ")
    numberList = []
    while userNumber != 'quit':
        numberList = [1,2,3,4]
        numberList.append(12)
        print(1,2,3,4,12)
        print('code is working- able to enter numbers')
        userNumber = input("Please enter a number: ")
    else:
        print('loop has ended. ')
        print('code is working- 404')

numberLoop()

i = 1
while i< 10:
    print(i)
    print("beginning of story")
    x = input("type something")
    print('middle of story')
    y = input("type something else")
    print('end of story')
    z = input("write 1 more thing")
    i += 1
    print(i)

def numberLoop():
    numberList = []
    userNumber = input("Enter a list of numbers")
    while userNumber != 'continue taking in a number':
        numberList = [1,2,3,4]
        userNumber = input("Please enter a number: ")
    else:
        print("loop has ended")
    