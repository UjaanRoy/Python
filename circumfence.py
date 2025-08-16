"""Raj is teaching maths to a class teacher of grade 10. Students are
facing difficulty in solving the circle problem. So for a better
understanding of students, he created a python function to calculate
the circumference of a circle.
Best of luck.
"""
def circle():
    radius = int(input("Write the radius of the circle: "))
    if radius < 0:
        print("Negative numbers are not applicable!")
    else:
        pi = 3.14159
        circumference = 2 * pi * radius
        print("The circumference of the circle is:", circumference)

print("This program lets you calculate the circumference of a circle with any radius.")
opinion = input("Do you want to try it out right now? ('n' for no and 'y' for yes): ")

if opinion == "n":
    print("Okay then...")
elif opinion == "y":
    circle()
else:
    print("The given answer is not applicable!")
