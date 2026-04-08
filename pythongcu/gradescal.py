a=int(input("enter marks: "))
b=int(input("enter marks: "))
c=int(input("enter marks: "))

p=(a+b+c)/300*100
print("percentage")
print(p)

if(p>=95):
    print("grade A")
elif(p>=50):
    print("grade B")
else:
    print("grade C")