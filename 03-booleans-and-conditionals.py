# # Boolean (True or False)
print("Example of boolean assignment")
x = True
print(x)
print(type(x))


# # Example of comparision operators
print("Example of comparision operators")
print(2 == 3)
print(2 != 3)
print(2 <= 3)
print(2 >= 3)

# # Example of a function with boolean check
print("Example of a function with boolean check")
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must "have attained to the Age of thirty-five Years"
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

# # Example Comparisons are a little bit clever
print("Example Comparisons are a little bit clever")
print(3.00 == 3)

# # Example Comparision are NOT to clever
print("Example Comparision are NOT to clever")
print('3' == 3)

# # Combining comparision operator with arithmetic operator
print("Combining comparision operator with arithmetic operator")

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

# # Combining comparision operators (and, or, not)
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))


# # Conditionals (if, elif, else)
print("Conditionals (if, elif, else)")
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

# # Boolean conversion
print("Boolean conversion example")
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

if 0:
    print(0)
elif "spam":
    print("spam")

# # Conditional expressions (aka 'ternary')
print("Conditional expressions (aka 'ternary') example")


def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)
quiz_message(80)

# You can combine this entire logic in single expression
def quiz_message(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)

quiz_message(45)
