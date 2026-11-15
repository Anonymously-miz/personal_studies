# # Variables are labeled boxes
# player_name = "Alex"       # str
# level = 12                 # int
# health = 98.6              # float
# is_alive = True            # bool

# print(f"{player_name} is level {level}")

# # Variables can change
# level = level + 1
# print(f"Level up! Now {level}")

# # Multiple assignment
# a, b, c = 1, 2, 3
# x = y = z = 0  # same value to many

# # Type checking
# print(type(health))  # <class 'float'>
# print(type(is_alive)) # <class 'bool'>

# # Common mistake: mixing types
# # print("Score: " + 100) # Error! Can't add str + int
# print("Score: " + str(100)) # Fix: convert

full_name = "Ishmail Abass Kamara"
birth_year = 2001
current_city = "Freetown"
loves_python = True
cash = 254.657

print(f"My name is {full_name}.\nI was born in {birth_year}.\ni currently lives in {current_city} and everybody know its {loves_python} that i love python")
print(type(full_name))
print(type(birth_year))
print(type(current_city))
print(type(loves_python))
print(type(cash))

age = "25"
print (age + str(1))
print (int(age) + 1)


