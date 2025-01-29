a=int(input("enter your salary:"))
b=int(input("enter your age: "))
if(a>=20000 and b<=25):
    c=input("enter your name:")
    d=input("enter your address: ")
    e=int(input("enter your req loan amount(max 50000):"))
    if(e<=50000):
        print("you are eligible for the loan")
    else:
        print("you are not eligible for the loan")
else:
    print("requirements are not satisfied")
