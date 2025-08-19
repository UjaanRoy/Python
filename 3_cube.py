"""Define a function to find a cube and define another function which let execute the cube 
function if the number is divisible by 3"""
def cube (number):
    number=number*number*number
    return number
def divide(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print (divide(12))
print (divide(5))
