"""Write to check a number is divisible by another number."""
input1=int(input ("Put the first number here:"))
input2=int(input ("Put the second number here:"))

if (input1%input2)==0:
    print (input1,"is divisible by",input2)
else:
    print (input1,"is not divisible by",input2)