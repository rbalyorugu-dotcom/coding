# Rock Paper Scissors game
# Should have a multiplayer function
# Menu selection


"Rock, Paper, Scissors game should have multiplayer"
"Users should be able to choose between rock, paper, and scissors"
"depending on their selection, they can either win, lose, or tie"
"rounds should go up to 4"
"If a player wins, you can take away a win from the opponent"
"could add it to yours"
"If you win 3 straight rounds its an automatic win"


"We could use strings to represent each option and possibly integers"

"the option"
"selection"
"example input 1 for rock, input 2 for scissor, input 3 for paper"
"analyis = easy"

"2 for scissor, input 3 for paper"
"We can use a comparison operator to compare who won more rounds."
"We can use a loop to keep the game going  until someone wins."

"if function; user gets 3 wins in a row consecutively, stops the game."

# design
# plan for how the program will "flow"; essentially, how will users
# use the program step-by-step

'Step. 1: Welcome the users to the game'
'Step. 2: Give them the option to play the game or see the game rules'
'Step. 3: if user select rules, show them the rules, else start the game'
'Step. 4: Inform the user the game has started and ask them to make a selection; R,P,S'
'Step. 5: Computer makes a random selection'
'Step. 6: determine and the user/player if they won, lose, or tied'
'Step. 7: (LOOP)  Show the user the RPS options and they will continue to play up '

# development

def RPSgame():
    RPSoptions = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissor: the game!")
print("Please select one of the following: ")
print("Enter p to start game.")
print("Enter r to see the  rules.")
selection = input()
if selection == 'r':
    print("here are the game rules...")
elif selection == 'paper':
    print("the game is starting...")
    choiceUser = input("please make selection, r=rock, p=paper, s=scissor")
    choiceCPU = random.choice(RPSoptions_cpu)
    # make a way to show the full selection word ; example: if s, the program should print scissor
    print("user selected: " + choiceUser)
    print("CPU selected: "+ choiceCPU)
    if choiceUser = "r"
       selectWord = "rock"
       print("user selcted: " + selectWord)
    elif choiceUser = "p"
        selectWord = "paper"
        print("user selected: " + choiceUser)
        print("CPU selected: "+ choiceCPU)
    elif 
else:
    print("Sorry, we didn't understand your entry.")


RPSgame()