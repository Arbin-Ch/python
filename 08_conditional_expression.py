# conditional expressions = A one-line shortcut for the "if_else_statement" (ternary operator)
# print or assign of two values based on condition
            #      X if condition else Y


num = float(input("Enter a number: "))
print("Positive" if num > 0 else "Negative")


num = int(input("Enter a number: "))
print("EVEN" if num % 2 == 0 else "ODD")


a = 6
b = 7

# max_num = a if a > b else b
min_num = a if a < b else b

# print(max_num)
print(min_num)


age = 12

status = "ADULT" if age >=18 else "CHILD"
print(status)


user_role = "user"          # admin or user

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)


temp = 20                 # you can change the temperature

weather = "HOT" if temp >= 25 else "WARM"
print(weather)
