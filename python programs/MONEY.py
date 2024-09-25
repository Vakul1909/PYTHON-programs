n= int(input("ENTER AMOUNT OF MONEY="))
a=n//2000
print("2000=",a)
b=n-a*2000
c=b//500
print("500=",c)
d=b-c*500
e=d//200
print("200=",e)
f=d-e*200
g=f//50
print("50=",g)
''
l1=[[1,2,3],[4,5,6]]
l2=[[11,12,13],[66,44,55]]
r1=len(l1)
r2=len(l2)
l3=[]
print(l1,"\n",l2)
if r1!=r2:
    print("Addition is not possible")
else:
    for i in range(0,r1):
        s=[]
        for j in range(0,r2):
            n=l1[i][j]+l2[i][j]
            s.append(n)
        l3.append(n)
print("Addition of list")
print(l3)
