n=int(input("ENTER NUMBER FOR MULTIPLICATION TABLE="))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
l1=[1,2,3,3,3,4,3,9]
print(l1)
print("1.pop\n2.clear\n3.reverse\n4.ascending\n5.descending\n6.count\n7.remove\n8.index")
choice=int(input("choose from above"))
if choice==1:
    c=l1.pop()
    print(c)
elif choice==2:
    c=l1.clear()
    print(l1)
elif choice==3:
    c=l1.reverse()
    print(l1)
elif choice==4:
    c=l1.sort()
    print(l1)
elif choice==5:
    c=l1.sort(reverse=True)
    print(l1)
elif choice==6:
    a=int(input("enter for count"))
    c=l1.count(a)
    print(c)
elif choice==7:
    b=int(input("enter no. for remove"))
    c=l1.remove(b)
    print(l1)
elif choice==8:
    d=int(input("enter value for index"))
    c=l1.index(d)
    print(c)
else:
    print("invalid entry")

