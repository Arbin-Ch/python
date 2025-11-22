# variable is a container for a value(string, integer, float, boolean)
# A variable behaves as the value that it contains

# string is a series of characters. it includes letters, numbers, symbols
# string is enclosed in single or double quotes

first_name = "coder"
food = "pizza"
email = "example@fake.com"

print(f"Hello {first_name}.")
print(f"My favourite food is {food}.")
print(f"My email is {email}.")


# An integer is a whole number. It can be either positive or negative. It cannot be in quote.

age = 25
quantity = 5
num_of_students = 30

print(f"My age is {age}.")
print(f"You're buying {quantity} item.")
print(f"There are {num_of_students} students in the class.")


# float is a decimal number. It can also be either positive or Negative. It must have decimal point.

price = 19.99
gpa = 3.2
distance = 10.5

print(f"The price of the item is ${price}.")
print(f"I got {gpa}  gpa in exam")
print(f"You ran {distance} km.")


# A Boolean is a datatype that can be either "True" or "False" Mostly it is used conditions.

is_student = True
if is_student:
    print("He is a student.")
else:
    print("He is not a student.")


is_sale = False
if is_sale:
    print("The item is on sale.")
else:
    print("The item is not on sale.")