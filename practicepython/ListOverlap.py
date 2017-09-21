#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,22,33,10,10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,33,33,33,33]
c=[]
Length_A=len(a)
Length_B=len(b)


if(Length_A>Length_B):
  print("The count of A is Higher, Taking A as primary list")
  for loopValue in a:
      if(loopValue in b and loopValue not in c):
          c.append(loopValue)

else:

  print("The count of B is Higher, Taking B as primary list")
  for loopValue in b:
      if(loopValue in a and loopValue not in c):
          c.append(loopValue)
print(c)

