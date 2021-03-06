# # Help function to help other functions
# Displays header and short description
print("Help function to help other functions")
help(abs)
help(round)


# # Defining a function to find least difference
print("Defining a function example")
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

# Help function telling something about least_difference function
help(least_difference)


# # Docstrings : The docstring is a triple-quoted string
# (which may span multiple lines) that comes immediately after the header of a function.
# When we call help() on a function, it shows the docstring.
print("Docstrings example")
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


help(least_difference)


# # Functions that don't return
# Return value from these functions are None which is null in other languages like java
print("None returning functions example")
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

# How to check this? print() does not return anything
mystery = print()
print(mystery)

# # Default arguments
print("Default arguments example")
print(1, 2, 3, sep=' < ')


# # Defining default argument
print("How to define default argument")
def greet(who="Colin"):
    print("Hello, ", who)


greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


# # Functions Applied to Functions
print("Functions Applied to Functions example")
def mult_by_five(x):
    return x * 5

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)


# # Functions that operate on other functions are called "Higher order functions."
print("Higher order functions example")
def mod_5(x):
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n'
)
