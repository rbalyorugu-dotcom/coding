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

print("checkingAccount" += paycheck * 0.5")
savingsAccount += paycheck * 0.25
retirementAccount += paycheck * 0.25

print("checkingAccount balance: += paycheck * 5" + str(checkingAccount))
print("savingsAccount balance: += paycheck / 4" + str(savingsAccount))
print("retirementAccount balance: += paycheck / 4" + str(retirementAccount))

payRate = 45
hours = 8
daysWorked = 5



payCheckFilter(payRate, hours, daysWorked)