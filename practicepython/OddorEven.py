#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

UserInput=int(input("Enter the number"))
check=int(input("Enter the value to check"))

if(UserInput%2==0):
        if(UserInput%4==0):
            print("The value give is a multiple of 4")
        else:
            print("The number you have entered is even")
else:
    print("The number you have entered is odd")

if(UserInput%check==0):
    print("The UserInput is divided by Check")
else:
    print("The UserInput is not divisible by Check")
