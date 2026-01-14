def payCheckFilter(payRate, hours, daysWorked):
    checkingAccount = 0
    retirementAccount = 0
    savingsAccount = 0

    paycheck = payRate * hours * daysWorked
    print("My paycheck for working "+ str(daysWorked) + " days will be $" + str(paycheck))

payCheckFilter(45, 8, 5)

payRate = 45
hours = 8
daysWorked = 5

paycheck = 1800

# print("checkingAccount" + paycheck * 0.5)
#savingsAccount += paycheck * 0.25
# retirementAccount += paycheck * 0.25

#print("checkingAccount balance: += paycheck * 5" + str(checkingAccount))
#print("savingsAccount balance: += paycheck / 4" + str(savingsAccount))
#print("retirementAccount balance: += paycheck / 4" + str(retirementAccount))

payRate = 45
hours = 8
daysWorked = 5



# payCheckFilter(payRate, hours, daysWorked)

def rideShareCalculator(miles, surgePrice, discount):
    base_fare = 3.00
    cost_per_mile = 2.00

    print("The final price for this ride is $" + str(base_fare + (miles * cost_per_mile)))
    if surgePrice == True:
        print("The final price for this ride is $" + str(base_fare + (miles * cost_per_mile)))
    else:
        print("The final price for this ride is $" + str(base_fare + (miles * cost_per_mile)))

    if discount == True:
        discount = total *.15
        total -= discount

rideShareCalculator(3, False, False)