def main():
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print(f"hello {to}")


main()
#strip() function remove white space on left and right but not between two word
#name = input("What is your name? ").strip().title()

#hello(name)
#print(f"Hello, {name}")

