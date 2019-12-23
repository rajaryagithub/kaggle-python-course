# Variable declaration and assignment
spam_amount = 0
# Function calling
print(spam_amount)

# Variable manipulation and operator overloading for string
spam_amount = spam_amount + 4

# Example of indentation
if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# To check the type of variable
print(type(spam_amount))

# True division as normal calculator
print(5 / 2)

# Division rounded down to next integer
print(5 // 2)

# Order of operation follows
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(-3 + 4 * 2)

# If default order fails then use parenthesis
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
print(max(1, 2, 3))
print(min(1, 2, 3))
print(abs(32))
print(abs(-32))

# Type converter functions
print(float(10))
print(int(3.33))
# Even a string which can be converted in number can also be used in these methods
print(int('807') + 1)
