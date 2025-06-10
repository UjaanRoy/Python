"""Radhika wants to design a program in which she can check that the character entered by the user is an
alphabet or not. So, write a program to identify the character."""
print ("This code checks what type of character (Only 1) you have assigned to a variable!")
user_value=input("Input a character:")
if user_value.isalpha():
    print ("The value you have assigned is a number!")
elif user_value.isdigit():
    print ("The value you have asssigned is an alphabet")
elif not user_value.isalpha() and not user_value.isdigit():
    print ("Special characters cannot be entered!")


