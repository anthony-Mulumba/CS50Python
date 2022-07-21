from msilib import type_string


def main():
    x = get_int_pass("What is the number? ")
    print(f"{x}")


#Here we don't prompt to the user the error faced but ordered him to enter again a number 3 times
#n=3 is a default value
def get_int_pass(prompt, n=3):
    value=1
    while value <= n:
        try:
            return int(input(prompt))
        except ValueError:
            value +=1
            pass
    return "You have entered three time non integer "
    
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