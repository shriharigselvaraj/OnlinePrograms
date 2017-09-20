#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly
# into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

userInput=int(input("Enter a number"))

for divisor in range(1,userInput):
    if(userInput%divisor==0):
        print("The Divisor for the user input "+str(userInput)+" is "+str(divisor))
