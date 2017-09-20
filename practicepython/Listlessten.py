# write a program that prints out all the elements of the list that are less than 5 or print new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

userInput=int(input("Enter a number"))
newList=[]
for b in a:
    if(b<userInput):
        print(b)
        newList.append(b)
print(newList)