"""An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
How it works:
Take a number.
Count how many digits it has.
Raise each digit to that power.
Add them up.
If the sum equals the original number, it's an Armstrong number!"""
a=int(input("Put a number here:"))
sum=0
temp=a
i=0
while temp>0:
    num=temp % 10
    sum += num**3
    temp //=10
if sum==a:
    print ("The given number is a armstrong number.")
else:
    print ("The given number is not a armstrong number.")

