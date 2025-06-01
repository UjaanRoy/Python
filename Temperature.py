print ("You can put the temperature in Fahrenheit to see which cloth is suitable to wear!")
Temperature = int(input("Put the temperature in Fahrenheit here-"))

if 35 <= Temperature <= 60:
    print ("With", Temperature, "Fahrenheit, you should wear a light to medium-weight jacket or sweater.")
elif 60 <= Temperature <= 80:
    print ("With", Temperature, "Fahrenheit, you should wear t-shirts, shorts, or light dresses.")
elif 80 <= Temperature <= 100:
    print ("With", Temperature, "Fahrenheit, wear the lightest clothes you have!")
elif Temperature >= 100:
    print ("I am starting to think you live on the sun...")
elif -20 <= Temperature <= 35:
    print("With", Temperature, "Fahrenheit, you should wear the heaviest clothes you have!")
elif Temperature <= -20:
    print ("I am starting to think you are in Antarctica!")






