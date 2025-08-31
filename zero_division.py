try:
    num1, num2=eval(input("Put two numbers to be assigned to the variables, and also put a comma seperating them :"))
    result= num1/num2
    print ("The result after deviding number 1 and 2 is",result)
except ZeroDivisionError:
    print ("You can't put zero as dividing with it will result in a error!")
except SyntaxError:
    print ("A comma is important to seperate both the numbers!")
except:
    print ("Wrong input! Please put a number to proceed...")
else:
    print ("No exceptions were found!")
finally:
    print ("This will print whatsoever...")