 # For loops
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(f"I love {fruit}")

# # range() is your best friend
# for i in range(5):  # 0 to 4
#     print(f"Count: {i}")

# for num in range(2, 11, 2):  # even numbers 2-10
#     print(num)

# # While loops
# count = 3
# while count > 0:
#     print(f"{count}...")
#     count -= 1
# print("Liftoff!")

# # Loop control
# for n in range(10):
#     if n == 3:
#         continue  # skip 3
#     if n == 7:
#         break     # stop at 7
#     print(n)

# # Real: sum of list
# numbers = [2,4,6,8]
# total = 0
# for n in numbers:
#     total += n
# print(f"Total: {total}")  # 20

# # print a triangle
# for i in range(1,6):
#     print('*' * i)
# print("#################")
# # reversed
# for i in range(5, 0, -1):
#    print('*' * i)


# # asking for a user input and printing its multiplication table

# user_number = int(input("enter number: "))
# for i in range(1,13):
#   print(f"{user_number} * {i} =  {user_number * i} ")

# # guessing game with while loop

# while True:
#   num = 4
#   guess = int(input("enter guess: "))
#   if guess == num:
#     print("you got it")
#     break
#   else:
#     print("guess again")
  
# # sum of all even numbers from 1 to 100
# total = 0
# for i in range(1,101,2):
#      total += i
# print(total)
total = 0
for i in range(2,101,2):
   total += i
print(total)




