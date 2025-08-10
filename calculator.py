"""Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly."""
def add(P,Q):
    return P+Q
def substract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q
print ("Choose one of the operations to be done-")
print ("a. Addition \n""b.Substraction \n""c.Multiplication \n""d.Division")
choice=input("Enter your choice here:")
num1=int(input("Enter number 1-"))
num2=int(input("Enter number 2-"))
if choice=="a":
    print (num1,"+",num2,"=",add (num1,num2))
elif choice=="b":
    print (num1,"-",num2,"=",substract(num1,num2))
elif choice=="c":
    print (num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print (num1,"/",num2,"=",divide(num1,num2))
else:
    print ("Invalid input has been entered...")
       