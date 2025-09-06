"""Write a program to check the age entered by the user is correct or not. If there is
some error in the value of age entered. And check that the age entered by the user is
even or odd."""

try:
    a=int(input("Enter your age:"))
    if a%2==0 or a==0:
        print ("Your age is a even number!")
    else:
        print ("Your age is a odd number!")
except ValueError:
    print ("You can only enter a number with no decimal numbers!")
    



