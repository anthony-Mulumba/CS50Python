def main():
    x= int(input("Enter the number of time: "))
    print_briks(x)

#def print_briks(n):
    #Print n briks in a row n time.
 #   for i in range(n):
  #      for j in range(n):
   #         print("#", end="")
    #    print()

def print_briks(size):
    #Print n briks in a row n time.
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


main()