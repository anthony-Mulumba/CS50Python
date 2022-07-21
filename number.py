def main():
    x = get_int_pass()
    print(f"You have entered: {x}")


#Here we don't prompt to the user the error faced but ordered him to enter again a number
def get_int_pass():
    while True:
        try:
            return int(input("Enter the number: "))
        except ValueError:
            pass

#Here the user received an error code when entering a non interger number
def get_int():
    while True:
        try: 
            x= int(input("Enter a number : "))
        except ValueError:
            print("Error ")
        else:
            return x
#print(f"You have entered the number {x}")

main()