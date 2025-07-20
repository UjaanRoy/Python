"""Write a program to print all the prime numbers which come in the range entered by the user?"""
lower_range=int(input("Put the starting point of the range here-"))
upper_range=int(input("Put the ending point of the range here-"))
print ("Prime numbers in the range are-")
for number in range (lower_range ,upper_range+1):
    if number>1:
        for i in range (2,number):
            if (number%i)==0:
                break
    else:
        print (number)
