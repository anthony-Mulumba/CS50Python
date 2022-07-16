def main():
    x= int(input("enter the value of x : "))
    if is_even(x):
        print(f"{x} is Even")
    else:
        print(f"{x} is Odd")

def is_even(n):
    return n%2 == 0
    #if n%2 == 0:
     #   return True
       # print(f"{n} is even")
    #else :
     #   return False
       # print(f"{n} is Odd")

main()
