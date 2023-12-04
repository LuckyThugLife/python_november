import random

num1 = random.randint(1, 20)

num2 = 0

while True:
    inp = int(input("enter a number from the 1st to the 20th "))
    num2 += 1
    
    
    if inp == num1:
        print(f"Congratulations! You guessed the number in {num2} attempts.")
        break

    if inp < num1:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")