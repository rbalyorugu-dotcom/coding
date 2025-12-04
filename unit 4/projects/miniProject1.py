def quiz():
    grade = 0
    multiple_choicequestions = ["Which of these is a multiple of 24", "What is the square root of 121", "Which is an example of potential energy", "Does hypotonic water cause fresh plant cells to swell", "Is 24 a multiple of 12"]
    print("Which of these is a multiple of 24?")
    A = print("A. 2")
    B = print("B. 18")
    C = print("C. 72")
    D = print("D. 1")
    userAnswer = input("Enter your answer:")
    correctAnswer = 'C'
    if userAnswer == correctAnswer:
        grade +=1
        print("Correct")
    else:
        print("Incorrect")
        grade -=1
    print("What is the square root of 121?")
    A = print("A. 13")
    B = print("B. 10")
    C = print("C. 9")
    D = print("D. 11")
    userAnswer = input("Enter your answer:")
    correctAnswer = 'D'
    if userAnswer == correctAnswer:
        grade +=1
        print("Correct")
    else:
        grade -=1
        print("Incorrect")
    print("What is an example of potential energy?")
    A = print("A. Holding a ball in the air")
    B = print("B. Pushing a box down a hill")
    C = print("C. pulling a crate across the floor")
    D = print("D. Throwing a football")
    userAnswer = input("Enter your answer:")
    correctAnswer = 'A'
    if userAnswer == correctAnswer:
        grade +=1
        print("Correct")
    else:
        grade -=1
        print("Incorrect")
    print("Does hypotoic water cause fresh plant cells to swell?")
    A = print("A. Yes")
    B = print("B. No")
    userAnswer = input("Enter your answer:")
    correctAnswer = 'A'
    if userAnswer == correctAnswer:
        grade +=1
        print("Correct")
    else:
        grade -=1
        print("Incorrect")
    print("Is 24 a multiple of 12")
    A = print("A. No")
    B = print("B. Yes")
    correctAnswer = 'B'
    userAnswer = input("Enter your answer:")
    if userAnswer == correctAnswer:
        grade +=1
        print("Correct")
    else:
        grade -=1
        print("Incorrect")
        print('here is your final grade: '+ str(grade) + '/ 5')
    
quiz()