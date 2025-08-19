"""Let's create a function total_calc() that helps us calculate and print out the total amount paid at 
a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a 
tip (tip_perc ), this function calculates the total amount you should pay."""
def total_calc (total,tip):
    total= total*(1+tip*0.01)
    total =round(total,2)
    return total
total=total_calc(150,20)
print (f"The total ammount to be paid is ,{total}")



