#Write a program to calculate the number of notes in the given amount?
Amount=int(input("Enter your number:"))
note_100=Amount//100
note_50=(Amount%100)//50
note_10=((Amount%100)%50)//10
coin_1=(((Amount%100)%50)%10)//1
print ("So, \nyou would need",note_100," note's' of hundred\n",note_50,"note's' of 50\n",note_10,"note's' of 10 and \n",coin_1,"coin's' of 1")