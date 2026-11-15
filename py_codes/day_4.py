# # Logic gates
# age = 20
# has_id = True

# # Simple if
# if age >= 18:
#     print("Adult")

# # if-elif-else chain
# score = 85
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "F"
# print(f"Grade: {grade}")

# # Combining conditions
# if age >= 18 and has_id:
#     print("Can enter club")
# elif age >= 18 and not has_id:
#     print("Need ID")
# else:
#     print("Too young")

# # Truthy / Falsy trick
# username = ""  # empty string is falsy
# if username:
#     print(f"Welcome {username}")
# else:
#     print("Username required")

# # Ternary
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# BMI CALCULATOR

# weight = float(input("enter weight in kg: "))
# height = float(input("enter height in m: "))

# b_m_i = weight/height
# print(b_m_i)

# if b_m_i < 18.5:
#     print("Underweight")
# elif 24.9 >= b_m_i >= 18.5:
#     print("Healthy Weight")
# elif 29.9 >= b_m_i >= 25.0:
#     print("Overweight")
# else: print("Obesity")

# login check
# username = "admin"
# password = "secret123"

# login_username = input("username: ")
# login_password = input("password: ")

# login_check = "Access granted" if login_username == username and login_password == password else "Access denied"

# print(login_check)

# leap year
# year = int(input("enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("leap year")
    
# else: print("not a leap year")