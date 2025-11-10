# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false , then answer the following questions: 

def neededhomeworkSubmissions():
    studentHomework = input("Enter homework assignments: ")
    homeworkAssignments = ["math homework", "english homework"]
    while studentHomework != neededhomeworkSubmissions
        if studentHomework < neededhomeworkSubmissions:
            print("Student has not submitted all assignments!")
            studentHomework = str(input("Please submit all assignments!")
        else:
            print("Student has submitted all assignments!")

neededhomeworkSubmissions()





# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

# hint: look into string reverse in w3schools

txt = "Summer is better than winter"[::-1]
print(txt)




# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

def guesstheNumber():
    correctNumbers = [8]
     userNumber = int(input("Please guess a number: "))
    while userNumber != 'correctNumber':
         if userNumber > 8:
             print("Error! The number you guessed was too high.")
            userNumber = int(input("Please guess a number: "))
        else:
            print("Error! The number you guessed was too low.")
            userNumber = int(input("Please guess a number: "))
    else:
        print("Congrats! You guessed the correct number.")
    
guesstheNumber()