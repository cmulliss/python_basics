from typing import cast


# animal = "cat"
# vegetable = "broccoli"
# mineral = "gold"

# print(animal + "\n" + vegetable + "\n" + mineral + "\n")

# Ex 2
# name = input("Enter your name: ")
# print("Your name is %s " % (name))
# print("\n")

# Ex 3
def cat_says(text):
    text_length = len(text)

    print("_" * text_length)
    print("<" + "%s" % (text) + ">")
    print("-" * text_length)
    print(" /")

    print(" /\_/\ /")
    print("( o.o )")
    print(" > ^ <")


def main():
    text = input("what does the cat say? ")
    cat_says(text)


if __name__ == "__main__":
    main()
