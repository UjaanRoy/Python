valid=False
while not valid:
    try:
        n=int(input("Enter a number (try entering a even number):"))
        while n%2==0:
            print ("Buh Bye!")
            value=True
    except ValueError:
        print ("Invalid input!")
    
