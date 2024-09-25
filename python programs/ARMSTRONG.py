n=int(input("ENTER A NUMBER"))
s=0
m=n
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if m==s:
    print("NUMBER IS ARMSTRONG NUMBER")
else:
    print("NUMBER IS NOT A ARMSTRONG NUMBER")
