# # Strings deep dive
# name = "  Ada Lovelace  "
# cleanName = name.strip()
# print(cleanName)        # Remove outer spaces
# print(cleanName.upper())        # ADA LOVELACE
# print(name.replace("Ada", "Grace")) # Grace Lovelace

# # Slicing magic
# lang = "Python"
# print(lang[0])    # P
# print(lang[-1])   # n
# print(lang[0:4])  # Pyth
# print(lang[::-1]) # nohtyP - reverse!

# # f-strings are king
# score = 95
# print(f"Score: {score} | Grade: {'A' if score>90 else 'B'}")

# # Numbers and Input
# # input() pauses and waits
# user_name = input("Your name? ")
# age_str = input("Age? ") # This is a string!
# age = int(age_str)
# print(f"In 10 years you'll be {age + 10}")

# # Useful math
# print(round(3.14159, 2)) # 3.14
# print(len("hello"))      # 5

# a program that accept user input and print initials
# full_name = input("Enter name: ")
# full_name_separated = full_name.split()
# first_initial = full_name_separated[0][0]
# Second_Initial = full_name_separated[1][0]
# third_Initial = full_name_separated[2][0]
# print(f"{first_initial}.{Second_Initial}.{third_Initial}")

# ask for 2 numbers and print sum, difference, product and power
# num1 = int(input('enter number: '))
# num2 = int(input("enter another number: "))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 ** num2)

# experiment with slicing
# greet = "Hello World"
# print(greet[3:8]) #lo wo

# madlibs game
# start = "My name is _________"
# print (start)
# name = input("enter name: ")
# print(start[0:10] +' '+ name + ".")
# middle = "I am _____ years old"
# print(middle)
# age = input("enter age: ")
# print(middle[0:4] + " " + age + " " + middle[-9:]+'.')
# end = "i want to be a _______"
# print(end)
# career = input("enter career: ")
# print(end[0:14] + " "+career + ".")


