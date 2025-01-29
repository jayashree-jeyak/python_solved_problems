a=int(input("enter your ENGLISH mark:"))
b=int(input("enter your MATHS mark:"))
c=int(input("enter your SOCIAL mark:"))
d=int(input("enter your SCIENCE mark:"))
e=int(input("enter your TAMIL mark:"))
average=(a+b+c+d+e)/5
print("your average is:",average)
if(average<=35):
    print("ADDITIONAL CLASS IS REQUIRED")
else:
    print("YOU ARE GOOD TO GO")
