def shutdown(user_opinion):
    if user_opinion.lower()=="yes":
        return "Shutting Down..."
    elif user_opinion.lower()=="no":
        return "Abort shutdown."
    else:
        return "Sorry, I didn't understand that"
response=input("Enter yes if you want to shut down the computer or no if you don't:")
print (shutdown(response))