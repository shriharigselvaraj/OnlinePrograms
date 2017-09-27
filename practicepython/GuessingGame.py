import random
sysGenValue=random.randint(0,9)
print("System value is "+str(sysGenValue))
userInput=int(input("Enter the value you guesses"))


for i in range(1,4):
  if(userInput>9):
    print("The value entered is beyoned the expected range")
  elif(userInput==sysGenValue):
    print("You won")
    break
  elif(userInput<sysGenValue):
    print("you have entered a value less than the system guessed")
    print("you still have "+str(4-i)+" attempts")
    userInput=int(input("Enter the value you guesses"))
  else:
    print("You have entered a value greater than the system guessed")
    print("you still have "+str(4-i)+" attempts")
    userInput=int(input("Enter the value you guesses"))
  print("You have given 3 attempts and you lost the game")
