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