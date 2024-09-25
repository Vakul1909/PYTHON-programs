'''
n=int(input("ENTER A NUMBER"))
s=0
m=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if m==s:
    print("NUMBER IS PALLINDROME")
else:
    print("NUMBER IS NOT A PALLINDROM")

num=int(input("Enter any number="))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("the factorial of",num,"=",fact)
'''

n=int(input("Enter decimal number="))
binarynum=[0]*n
i=0
while(n>0):
    binarynum[i]=n%2
    n=int(n/2)
    i+=1
for j in range(i-1,-1,-1):
    print(binarynum[j],end="")


number = int(input(" Please enter any Number : "))
fact = 1

for i in range(1, number + 1):
    fact = fact * i
print("The factorial of",number,"=",fact)

n= int(input("Enter decimal number"))
     

binaryNum = [0] * n;
 

i = 0;
while (n > 0):

        binaryNum[i] = n % 2;
        n = int(n / 2);
        i += 1;
 

for j in range(i - 1, -1, -1):
        print(binaryNum[j], end = "");

d={}

n=int(input('Enter number of the winners :'))

for i in range (n):

   a=input('Enter name of the winner:')

   b=int(input('Enter the number of wins of the winner:'))

   d[a]=b

print('\n')

print('name of the winners','\t','number of wins')

for i in d:

   print(i,'\t','\t','\t',d[i])

print('\n')
'''

val=int(input('Enter the value to be checked:'))

for i in (d.values()):

   if val==i:

       print('found')

       break

else:

   print('not found')
Lst1 = eval(input("enter unsorted values in the list"))
n = len(Lst1)
s = int(input("Enter a number to Search"))
flg = False
index=0
for i in range (0,n):
    if Lst1[i] == s:
        flg=True
        index=i
    if flg==True:
        print("Successful Search. Number Found at ", index, " index")
else:
    print("Unsuccessful Search. Number Not Found")''
input()
lst1 = [12,8,99,81,14,7]
n = len(lst1)
i = 1
count = 0
while i<n:
    for j in range (0,i+1):
        if lst1[i]<lst1[j]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
            count += 1
        #print(lst1[j],end= ' ')
    i += 1
    #print()
print("Sorted List is ")
print(lst1)
print("Total Swaps = ",count)''

l1=[[1,2,3],[4,5,6]]
l2=[[11,22,33],[66,44,55]]
r1=len(l1)
r2=len(l2)
l3=[]
print(l1,"\n",l2)
if r1!=r2:
    print("Addition is not possible due to size")
else:
    for i in range(0,r1):
        s=[]
        for j in range(0,r2):
            n= l1[i][j] + l2[i][j]
            s.append(n)
        l3.append(s)
print("addition of list")
print(l3)'


l1=[[11,12,13],[44,55,66],[98,89,99]]
s=0
for i in range (0,3):
    for j in range (0,3):l1=[12,55,66,77,44,67,89]
big=0
for n in l1:
    if big<n:
        big=n
print("biggest element is",big)'



l1=[[1,2,3],[4,5,6],[7,8,9]]
r1=len(l1)
n=r1
m=n
for i in range(0,r1):
    n=m
    for j in range(0,n):
        print(l1[i][j], end=' ')
    print()
    m-=1'''
D={1:'html',2:'python',3:'java',4:'C++'}
k=list(D.keys())
v=list(D.values())
for i in range (0,len(D)):
    print(k[i],':',v[i])

