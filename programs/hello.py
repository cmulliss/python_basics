first_character = "Hello"[0]

print("The first character is: ", first_character.lower())
print("The first character is: ", first_character)

fruit = "banana"
print(len(fruit))

# string concatenation
print("I " + "love " + "python.")

# variable concatenation
first = "I "
second = "love "
third = "penguins!"

print(first + second + third)

# or better using format fn
print(f"{first}{second}{third}")

# Repeating strings

print("-" * 10)

happiness = "happy " * 3
print(happiness)

# the str() fn
print("I love python " + str(3) + ".")

print("{}{}{}".format("I ", "love ", "penguins"))

# can specify position of replacement

print("{2}{0}{1}".format("I ", "love ", "penguins "))
print("\n")
# specifying string widths and positions
# can use <^> to get alignment
print("{0:8} | {1:<8}".format("Fruit", "Quantity"))
print("{0:8} | {1:8.2f}".format("Apples", 3.3333))
print("{0:8} | {1:8.2f}".format("Oranges", 10))

print("\n")

# data types, floats and number of decimal places
