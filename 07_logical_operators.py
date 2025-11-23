# logical operator = It evaluates multiple conditions. (or, not, and)
# or = at least one condition must be True
# and = both of the condition must be True
# not = inverts the condition (not False, not True)


# Example of "or" logical operator
temp = 20
is_raining = True

if temp > 25 or temp < 0 or is_raining:
    print("The outdoor event is canceled!")
else:
    print("The outdoor event is still scheduled!")


# Example of "and" logical operator
temp = -1
is_sunny = True

if 25 < temp > 0 and is_sunny:
    print("It is Hot outside!")
    print("It is sunny!")
elif temp <= 0 and is_sunny:
    print("It is cold outside!")
elif 20 > temp > 15 and is_sunny:
    print("It is warm outside!")
    print("It is sunny!")


# Example of "NOT"

temp = 0
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is Hot outside!")
    print("It is CLOUDY !")
elif temp <= 0 and not is_sunny:
    print("It is cold outside!")
    print("It is CLOUDY !")
elif 20 > temp > 15 and not is_sunny:
    print("It is Warm outside!")
    print("It is CLOUDY!")