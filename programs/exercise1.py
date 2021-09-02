from typing import cast


animal = "cat"
vegetable = "broccoli"
mineral = "gold"

print(animal + "\n" + vegetable + "\n" + mineral + "\n")

# Ex 2
# name = input("Enter your name: ")
# print("Your name is %s " % (name))
# print("\n")

# Ex 3
catsays = input("What is the cat saying? ")
catsays_length = len(catsays)

print("_" * catsays_length)
print("<" + "%s" % (catsays) + ">")
print("-" * catsays_length)
