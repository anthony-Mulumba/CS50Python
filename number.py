while True:
    try: 
        x= int(input("Enter a number : "))
    except ValueError:
        print("Error ")
    else:
        break
print(f"You have entered the number {x}")