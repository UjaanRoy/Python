print ("You can put the temperature in Farenhiet to see which cloth is suitable to wear!")
Temperature=int(input("Put the temperature in farenhiet here-"))
if Temperature>35 and Temperature <60:
    print ("With",Temperature,"farenhiet, you should wear a light to medium-weight jacket or sweater.")
elif Temperature>60 and Temperature<80:
    print ("With",Temperature,"farenhiet, you should wear t-shirts, shorts, or light dresses.")
elif Temperature>80 and Temperature<100:
    print ("With",Temperature,"farenhiet,wear the lightest clothes you have!")
elif Temperature>100:
    print ("I am starting to think you live on the sun...")
elif Temperature<35 and Temperature>-20:
    print("With",Temperature,"farenhiet, you should wear the heaviest clothes you have!")
elif Temperature<-20:
    print ("I am starting to think you are in Antarctica!")





