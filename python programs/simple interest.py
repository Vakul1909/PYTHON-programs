p=int(input("ENTER PRINCIPLE AMOUNT-"))
r=int(input("ENTER RATE-"))
t=int(input("ENTER TIME(In year)-"))
si=(p*r*t)/100
print("SIMPLE INTEREST=",si)
t1=(12,1,3,3,3,14,15,16)
print(t1)
print("1.lenght\n2. For maximum value\n3. For minimum value")
choice=int(input("choose from above"))
if choice==1:
    c=len(t1)
    print("length",c)
elif choice==2:
    c=max(t1)
    print("maximum",c)
elif choice==3:
    c=min(t1)
    print("minimum",c)
elif choice==4:
    a=int(input("enter value"))
    c=t1.count(a)
    print(c)
elif choice==5:
    b=int(input("enter value"))
    c=index(b)
    print(c)
else:
    print("Invalid entry")
    
