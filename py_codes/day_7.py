# projects

# calculator
# steps involve are:
# ask for user inputs
# try to give user the option to add other numbers
# ask for operation
# calculate the math based on operation

# step 1
# calculate_again = True
# while calculate_again:
#     num1  = int(input("enter number 1: "))
#     print(num1)
#     num2  = int(input("enter number 2: "))
#     print(num2)

#     # step 2(skip for now)
  
#      # step 3
#     op = input("enter operation sign: ")
#     print(f"{num1} {op} {num2}:")

#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         if num2 == 0:
#             print("cannot divide by 0")
#         else:
#             print(num1 / num2)

#     choice = input("perform another operation(y/n): ")
#     if choice == 'n':
#         break

# number guessing game
import random

random_number = random.randint(1,50)
tries = 5
while tries > 0:
    print(f"you have {tries} tries to get the number\nGoodluck!")
    guess = int(input("enter a guessed number: "))
    if guess == random_number:
        print(f"you got it in {tries} tries\nThe number was {guess}")
        break
    elif guess > random_number:
        print("Too High")
        tries -=1
    else: 
        print("Too Low")
        tries -=1

    if tries == 0:
        print(f"you lost\nThe number was {random_number}")