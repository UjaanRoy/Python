"""Raj is a class teacher of grade 10. He wants to design a program that only allows students aged 10
to 20 years in his class. As a result, students whose age is more than 20 can not enrol in his class.
Best of luck"""
print("You will be allowed to the classroom only if you are older than 10 years and younger than 20 years!")
age=int(input("Put your age here:"))
if age>=10 and age<20:
    print ("Great! You are applicable for taking clases!")
else:
    print ("Sorry, your age is not applicable!")
