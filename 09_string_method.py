# name = input("Enter your name: ")
# result = len(name)                           # provides the length of string
# print(result)


# name = input("Enter your name: ")
# result = name.find("a")                       # provides the index of the first occurrence of specified value.
# print(result)                                 # If not found, it returns -1


# name = input("Enter your name: ")
# result = name.rfind("a")                        # provides the index of the last occurrence of specified value.
# print(result)                                   # If not found, it returns -1


# name = input("Enter your name: ")
# result = name.capitalize()                      # capitalize only the 1st word of the character
# print(result)


# name = input("Enter your name: ")
# result = name.upper()                            # convert all the small characters into capital characters
# print(result)


# name = input("Enter your name: ")
# result = name.lower()                               # convert all the capital characters into small characters
# print(result)


# name = input("Enter your name: ")
# result = name.isdigit()                             # checks if all character in the string are digits.
# print(result)                                       # output returns either True or False. spaces also gives False output



# name = input("Enter your name: ")
# result = name.isalpha()                             # checks if all character in the string are alphabets.
# print(result)                                       # output returns either True or False. spaces also gives False output


# phone_number = input("Enter your phone number: ")
#
# result = phone_number.count(" ")                     # counts how many times the specified value appears in the string
# result = phone_number.replace(" ", "")             # replaces the specified value with another value in string.
# print(result)
# print(result)


# Exercise: valid username input exercise
# 1). username is not more than 12 characters
# 2). username must not contain spaces
# 3). username must not contain digits

username = input("Enter the username: ")

if len(username) > 12 :
    print("Your username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can't contain digits.")
else:
    print(f"Welcome {username}!")