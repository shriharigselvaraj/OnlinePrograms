userInput=str(input("Enter the sentence"))
splited=userInput.split(" ")
orderRev=splited[::-1]
print(' '.join(orderRev))
