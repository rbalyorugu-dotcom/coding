# Operators
# Operators are a construct (built-in system) that give
# Print() is a function where anything inside the round brackets
# will be printed out in the terminal
# data types more actions and power.

# Arithmetic Operator Family
# Arithmetic operators are simply math operators
# We use mathematical symbols such as the addition, subtraction,
# multiplication and division sign to do operations.

print(2 + 3)
print(20 - 100)
print(40 / 2)
print(30.9 * 10)

# Assignment Operator Family
# These operators assign values to variables
# (otherwise known as containers)
# key - value pairs

# variable = container for data.

schoolName = "Boys Latin High"
age = 16

age += 1.5

age -= 3

number = 3

print(age + number) #19

print(2>1)





print(2!= 3) # NOT the same

# Logical Operator Family
# it checks and compares if certain code conditions are true or false

print(3 > 1 and "Robert" == "Robert")
# the AND operator checks to see BOTH conditions are true.
# If BOTH are TRUE the answer is TRUE.

print(2 == 1 or 3 > 2)
# the AND operator checks to see if ONE of the conditions is TRUE.
# So long as ONE of the conditions is TRUE, it will be TRUE.

print(not(3 > 1 and "Robert" == "Robert"))
#The NOT operator will give the oposite result.
# the NOT operator flips the result.

algebraPassed = True
historyPassed = True

# does this person need credit recovery
# true means they passed
print(not(algebraPassed== True and historyPassed == True))