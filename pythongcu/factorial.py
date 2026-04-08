a=int(input("enter any number "))
for i in range (1,a+1):
    if i==1:
        factorial=1
    else:
        factorial=factorial*i
print("factorial of",a,"is",factorial)
