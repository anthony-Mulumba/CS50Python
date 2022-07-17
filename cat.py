def main():
    number = get_number()
    meow(number)

#Funtion to get a number
def get_number():
    while True:
        n=int(input("Enter a positive number: "))
        if n > 0:
            break
    return n

#Funtion to print meow n times
def meow(n):
    for _ in range(n):
        print("meow")

main()

#Loop
#i = 3
#while i!= 0:
 #   print("meow")
  #  i = i-1
#print("\n")
#print("mewo \n" * 3, end="")

#Infinite loop until a condition is made to break it

#while True:
 #   n=int(input("Enter a positive number: "))
  #  if n > 0:
   #     break

#for _ in range(n):
 #   print("meow")
