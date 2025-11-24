# while loop: execute some code WHILE some condition remains True

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
#
# print(f"Your name is {name}")


# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
#
# print(f"Your are {age} years old")


food = input("Enter the food you like? (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter the another food you like? (q to quit): ")

print("BYE!")


# num = int(input("Enter the number 1 to 10: "))
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter the number 1 to 10: "))
#
# print(f"You number is {num}")