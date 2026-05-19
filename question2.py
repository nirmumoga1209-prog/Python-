a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

# Sum of any two sides must be greater than the third
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid")
else:
    print("Invalid")