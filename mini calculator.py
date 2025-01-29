a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=input("choose operation: add/sub/mul/div: ")
if(c== "add"):
    print(c,a+b)
elif(c=="sub"):
    print(c,a-b)
elif(c=="mul"):
    print(c,a*b)
elif(c=="div"):
    print(c,a/b)
else:
    print("operation is invalid")
