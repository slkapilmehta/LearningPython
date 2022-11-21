import random

randomNumber = random.randint(0, 9)

enteredNumber = input("enter number :")
enteredNumber = int(enteredNumber)
if enteredNumber > 9:
    print("wrong value entered, enter between 0 and 9")
else:
    if enteredNumber == randomNumber:
        print("correct guess")
    else:
        print("wrong guess")