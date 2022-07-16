name = input("What's your name? ")

match name:
    case "Anthony" | "Aurelie" | "Bryan" | "Nolhan":
        print("Joli Parc")
    case _:
        print("Mboloko")