# created 3 variables
num1 = 10
num2 = 3
num3 = 8


# creating additional variables to assign it 
# the result of the values of logical operators
num4 = num3 < num2 and num1 < num2 # False
num5 = num1 < num3 or num3 < num3 # False
num6 = not(num3 < num2 and num1 < num2) # True

# output the result
print(num4)
print(num5)
print(num6)