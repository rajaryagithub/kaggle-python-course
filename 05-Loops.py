# # Loops example
print("Loops example")
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')  # print all on same line

# Set of values can also be a tuple
print("Tuple in loop example")
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

# Can loop through chars of a string
print("Chars of string in loop example")
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')


# # range() is a function that returns a sequence of numbers
print("\nrange() examples")
for i in range(5):
    print("Doing important work. i =", i)


# # while loop, which iterates until some condition is met
print("while loop examples")
i = 0
while i < 10:
    print(i, end=' ')
    i += 1


# # List comprehensions example
print("List comprehensions example")
squares = [n**2 for n in range(10)]
print(squares)
# To acheive this we have to do this much
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

# We can also add if statement
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)


# # List comprehensions combined with functions like min, max, and sum
print("List comprehensions combined with functions like min, max, and sum")

# Normal implementation
def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
numbers = [5, -1, -2, 0, 3]
print(count_negatives(numbers))

# Here's a solution using a list comprehension
def count_negatives(nums):
    return len([num for num in nums if num < 0])
numbers = [5, -1, -2, 0, 3]
print(count_negatives(numbers))

# This looks best of all three solutions
def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
numbers = [5, -1, -2, 0, 3]
print(count_negatives(numbers))

