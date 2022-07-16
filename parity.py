def main():
    x= int(input("enter the value of x : "))
    is_even(x)

def is_even(n):
    if n%2 == 0:
        print(f"{n} is even")
    else :
        print(f"{n} is Odd")

main()
