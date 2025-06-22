"""Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?"""
a=10
b=20
c=30
average=(10+20+30)/3
print ("The average is",average)
if a<average:
    print ("The first cyclist is slower than the rest.")
elif b<average:
    print ("The second cyclist is slower than the rest.")
elif c<average:
    print ("The third cyclist is slower than the rest.")