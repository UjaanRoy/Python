# Decimal to Binary Conversion using while loop

decimal = int(input("Write a decimal number which you want to convert to a binary number: "))
binary = ""

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("Binary number is:", binary)
