"""Write a program to understand how the value error exception works."""
try:   
    number=int(input("Enter a number here:"))
    print ("The number is",number)
except ValueError as ex:
    print ("Except",ex)
