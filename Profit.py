"""Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?"""
print ("The orange's original price was 100 rs!")
Original_value=120
Resell_value=int(input("Give your resell value:"))
if Original_value>Resell_value:
    print ("Loss!")
elif Resell_value>Original_value:
    print ("Profit!")
else:
    print ("No profit no loss!")
   