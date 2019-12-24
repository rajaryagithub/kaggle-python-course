# Variable declaration and assignment
spam_amount = 0
# Function calling
print("Variable assignment")
print(spam_amount)

# Variable manipulation and operator overloading for string
print("Variable manipulation and operator overloading for string")
spam_amount = spam_amount + 4

# Example of indentation
if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# To check the type of variable
print("To check the type of variable")
print(type(spam_amount))

# True division as normal calculator
print("True division as normal calculator")
print(5 / 2)

# Division rounded down to next integer
print("Division rounded down to next integer")
print(5 // 2)

# Exponentiation
print("Exponentiation example")
print(5 ** 2)

# Negation
print("Negation example")
a = 4
a = -a
print(a)

# Order of operation follows
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print("# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")
print(-3 + 4 * 2)

# If default order fails then use parenthesis
print("Parenthesis example")
hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
# Failed
print("Height in meters =", total_height_meters, "?")
# Corrected
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Built in methods for number
print("Built in methods for number")
print(max(1, 2, 3))
print(min(1, 2, 3))
print(abs(32))
print(abs(-32))

# Type converter functions
print("Type converter functions")
print(float(10))
print(int(3.33))
# Even a string which can be converted in number can also be used in these methods
print(int('807') + 1)
