#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the
# year that they will turn 100 years old.
from builtins import input

name=input("Enter your name\n")
age=int(input("Enter your age"))
repeat=int(input("Enter the number of time the message should be displayed"))

if(age<101):
    print(repeat*(name+", You are going to turn 100 in "+str(100-age)+"\n"))
else:
    print(repeat*("You are already crossed 100 years, All the best \n"))