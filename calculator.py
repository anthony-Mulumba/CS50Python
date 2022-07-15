def main():
    x = int(input("What is the square of : "))
    print(f"The square of {x} is", square(x))

def square(n):
    return n*n

main()

#strip() function remove white space on left and right but not between two word
#name = input("What is your name? ").strip().title()
#print(f"Hello, {name}")
#Calculator
#nb1 = float(input("Enter first number : "))
#nb2 = float(input("Enter second number : "))
#print(round(nb1 + nb2, 2))

