# importing the module random
import random

# generating a random number from 1 to 20
secretNum = random.randrange(1,20)

# looking for the secret number using the 
# while loop and breaking the loop using break
    
i = 1
while i < secretNum :
    i += 1    
    if i == secretNum:
        print("Congratulations! The secret number is " + str(secretNum))       
        break

# var 2. without break
"""i = 1
while i < secretNum :
    i += 1
else:
    print("Congratulations! The secret number is " + str
          (secretNum))"""
    

