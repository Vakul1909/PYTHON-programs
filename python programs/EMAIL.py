'''
e=input("ENTER YOUR EMAIL:")
special=False
for ch in e:
    if ch=="@"or ch==".":
        special=True
if special==True:
    print("EMAIL IS VALID")
else:
    print("EMAIL IS INVALID")
    
s1=input("enter a string")
n=len(s1)
for ch in s1:
    if ch=='a'and ch=='z':
        print(chr(ord(ch)-32),end='')
    elif ch>='A'and ch<='Z':
          print(ch,end='')
'''          
s1=input("ENTER PASSWORD=")
n=len(s1)
letter=False
special=False
upper=False
for ch in s1:
    if ch.isdigit():
       letter=True
    elif ch.isalnum():
        special=True
    elif ch.islower():
        upper=True
if letter==True and special==True and upper==True and n>=8:
    print("password is good")
else:
    print("bad password")
''
def sum(a,b):
    c=a+b
    print("addition=",c)
a=int(input("enter value1"))
b=int(input("enter value2"))
sum(c)

         
         
        
    




