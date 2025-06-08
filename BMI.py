#BMI = weight (kg) / height² (meters)
Height=float(input("Please put your body height in meters:"))
Weight=float(input("Put your body weight in kg:"))
BMI= Weight/Height**2
print ("Your BMI is-",BMI)
if BMI<18.5:
    print ("You are an underweight!")
elif BMI>=18.5 and BMI<24.9:
    print ("You have a normal weight")
elif BMI>=24.9 and BMI<29.9:
    print ("You are an overweight.")
else:
    print ("You are obese.")