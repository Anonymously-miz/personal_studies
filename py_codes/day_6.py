# # Lists - mutable backpack
# shopping = ["milk", "bread", "eggs"]
# print(shopping[0]) # milk

# shopping.append("butter")      # add end
# shopping.insert(1, "cheese")   # insert at index 1
# print(shopping)

# shopping.remove("bread")  # by value
# last = shopping.pop()     # removes last and returns it
# print(f"Removed: {last}")
# shopping.sort()
# print(shopping)

# # List comprehension preview
# squares = [x**2 for x in range(5)]  # [0,1,4,9,16]

# # Tuples - immutable locked box
# coordinates = (10.5, 20.3)
# # coordinates[0] = 99 # ERROR!
# print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# # Unpacking
# x, y = coordinates
# name, age = ("Alice", 30)

# # Why tuples? Dictionary keys and safety
# # list can't be dict key, tuple can
# locations = {(0,0): "origin", (1,1): "center"}
# print(locations[(0,0)])

# print(len(shopping))

# # a list of 5 friends
# friends = ['Alhaji', 'Michael', 'Kalie', 'Gibrilla', 'Hawa']

# # add a friend at an index and another at the end
# friends.insert(4, 'Prince') # inserted prince at index 4
# friends.append("hafsatu") # added hafsatu at the end of the list

# # removing a particular friend
# friends.remove('Hawa') #removed hawa from last

# # removing the last friend
# friends.pop()
# friends.sort()
# print(friends)

# # a tuple of my birthdate (year, month, day)
# birthDate = (2001, 10, 18)

# an attempt to modify an immutable tuple
# birthDate[2] = 14 #error

# create a new list from a list by multiply every element in the last by 2

# numbers = [1,2,3,4,5]
# new_numbers = []

# for number in numbers:
#     # result=numbers* 2
#     result = number * 2
#     new_numbers.append(result)

# # print(result)
# print(new_numbers)

numbers = [3,9,7,1,6]
# for number in numbers:
    # if number == max(numbers):
    #     numbers.remove(number)
    #     print(max(numbers))



largest = numbers[0] # first item
second_largest = numbers[1] #second item

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("Second largest:", second_largest)