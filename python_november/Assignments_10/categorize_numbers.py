# The source of the data list
number_list = [3, 7, 12, 5, 9]

# creating a c function with a single argument
def categorize_numbers(num):

    for x in num: # iterate through each item in the list
        if x > 10: # setting selection criteria
            print("High Number")
        elif x < 5:
            print("Low Numbe")
        else:
            print("Medium Number")


# calling a function with incoming data from the source data list
categorize_numbers(number_list) 