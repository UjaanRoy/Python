print ("This code is to check if you are eligible for giving this upcoming exam.")
print ("You will only be allowed if you have any medical concerns or if your attendance is higher than %70")
medical_state=input("Only answer with 'y' for yes and 'n' for no if you have medical concerns=")
if medical_state.lower() =="y":
    print("Great! You are eligible for giving this exam!")
else:
    print ("As you have no medical states, your eligibility depends on you attendance.")
    att=int(input("Put your attendance rate="))
    if att>=75:
        print("Great! You are eligible for giving this exam!")
    else:
        print ("Sorry, you are not eligible for this exam.")

