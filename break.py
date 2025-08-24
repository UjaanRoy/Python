user_word=input("Write any one word to see if it has the letter 'A':")
for i in user_word.lower():
    if (i=='a'):
        print ("A is found!")
        break
    else:
        print ("A is not found!")
