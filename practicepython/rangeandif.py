#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

number=range(2000,3200)
finalList=[]

for calc in number:
  if(calc%7==0 and calc%5!=0):
    finalList.append(calc)
print(finalList)
