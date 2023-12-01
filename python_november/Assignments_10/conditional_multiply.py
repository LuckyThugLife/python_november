# The source of the data list
number_list = [3, 7, 12, 5, 9]
# multiplier
multiply_factor = 2

# creating a function with 2 arguments
def conditional_multiply(num, mult):

    for x in num:  # iterate through each item in the list
      if x > 5: # setting selection criteria
        print(x * mult)
      elif x <= 5:
        print("that the number is not multiplied.")

# calling a function with incoming data from 
# a list of source data and a multiplier
conditional_multiply(number_list,multiply_factor)