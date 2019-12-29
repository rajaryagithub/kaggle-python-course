# # Lists are objects stored in a sequence
print("Lists are objects stored in a sequence")

primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(primes)
print(planets)

# We can also have list of lists
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
print(hands)

# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
print(hands)

# List can contain mix type of data as well
my_favourite_things = [32, 'raindrops on roses', help] # here "help" is a function in the list
print(my_favourite_things)


# # Indexing examples
print("Indexing examples")
print("Indexing starts from 0 (zero)")
planet = planets[0]
print(planet)

# Next element
planet = planets[1]
print(planet)

# Element at the end can be accessed using negative indexes
# Last element
planet = planets[-1]
print(planet)
# Second last element
planet = planets[-2]
print(planet)


# # Slicing example
print("Slicing example")

# Starting index and the end index (but it does not include last index value)
print(planets[0:3])

# The starting and ending indices are both optional
print(planets[:3])
print(planets[3:])

# We can also use negative indices when slicing
# All the planets except the first and last
print(planets[1:-1])

# The last 3 planets
print(planets[-3:])


# # changing lists
print("Changing lists examples")
planets[3] = 'Malacandra'
print(planets)

# Changing some list members in one go
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)


# # List functions
print("List functions examples")

# How many planets are there? len function gives length of list
print(len(planets))

# sorted returns a sorted version of a list, by default ascending
print(planets)
sorted_planets = sorted(planets)
print(sorted_planets)

# sorting in descending order
print(planets)
desc_sorted_planets = sorted(planets, reverse=True)
print(desc_sorted_planets)

# sum is also good for number list to sum
primes = [2, 3, 5, 7]
print(sum(primes))

# max or min also works for number list
print(min(primes))
print(max(primes))


# # Attributes and methods of an object (actually everything in python is object) examples
print("Attributes and methods of an object (actually everything in python is object) examples")
x = 12
# x is a real number, so its imaginary part is 0
print(x.imag)

# Here's how to make a complex number, in case you've ever been curious
c = 12 + 3j
print(c.imag)

# We access methods or attributes using dot (.) operator
print(x.bit_length)

# To actually call it we use parentheses
print(x.bit_length())


# # List methods examples
print("List methods examples")
# list.append modifies a list by adding an item to the end
# Pluto is a planet darn it!
planets.append('Pluto')
print(planets)

# list.pop removes and returns the last element of a list
last_planet = planets.pop()
print(last_planet)
print(planets)

# # Searching list examples
print("Searching list examples")
# Finding index of an element
index_of_element = planets.index("Earth")
print(index_of_element)

# What if an element is not in list? Uncomment and run to see the error.
#index_of_element = planets.index("Pluto")
#print(index_of_element)
# Avoid this error using 'in' operator
is_element_available = "Pluto" in planets
print(is_element_available)
is_element_available = "Earth" in planets
print(is_element_available)

# Use help to see all available methods on list. Uncomment and run to see the list.
#help(planets)


# # Tuples examples
print("Tuples examples")
# Tuples are almost exactly the same as lists. They differ in just two ways.
# 1st: The syntax for creating them uses parentheses instead of square brackets
t = (1, 2, 3)
print(t)
# equivalent to above
t = 1, 2, 3
print(t)

# 2nd: They are immutable. Uncomment and run to see the error.
#t[0] = 100

# Tuples are often used for functions that have multiple return values.
x = 0.125
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator, numerator / denominator)


# # A python trick to swap the values
print("A python trick to swap the values")
a = 1
b = 2
a, b = b, a
print(a, b)
