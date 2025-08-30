"""Vishal goes out to buy some household items and the total bill was 2.50$. 
He did not have change so he paid 4$. So, now he wants to calculate 
the shopkeeper should return to him."""
total=float(2.50)
Total_paid=float (4)
to_be_returned=(Total_paid-total)

for i in range (3):
    if i==0:
        continue
    if i==1:
        pass
        print("So, $",to_be_returned,"is to be returned by the shopkeeper!")
        break
