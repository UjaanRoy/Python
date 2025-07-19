"""Write a program to calculate how many total digits are in a number entered by the
user?
"""
number=int(input("Put a number here-"))
count=0
if number==0:
    count=1
while number>0:
    number=number//10
    count+=1
print ("Total digits are",count)
