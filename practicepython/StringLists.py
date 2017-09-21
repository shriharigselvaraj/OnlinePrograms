#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

userInput=str(input("Enter a word"))
revUserInput=userInput[::-1]

if(userInput==revUserInput):
    print("Entered value is palindrome")
else:
    print("Entered value is not a palindrome")
