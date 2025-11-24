# indexing = accessing elements of a sequencing using [] indexing operator
#            [start: end: step]

credit_number = "1234-5678-9012-3456"

# Accessing single digits:
first_digit = credit_number[0]
print(first_digit)

last_digit = credit_number[-1]
print(last_digit)

# Accessing substring
middle_digit = credit_number[1:-1]
print(middle_digit)

more_digit = credit_number[5:8]
print(more_digit)

# Accessing with steps:
other_digit = credit_number[::3]
print(other_digit)

extra_digit = credit_number[::5]
print(extra_digit)

# last digit of credit number:
credit_number = "1234-5678-9012-3456"
last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

# Reversing the string
credit_number = "1234-5678-9012-3456"
reverse_digit = credit_number[::-1]
print(reverse_digit)