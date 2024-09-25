
n=input("NAME-")
r=int(input("ROLL NUMBER-"))
print("MARKS")
e=int(input("ENGLISH MARKS-"))
h=int(input("HINDI MARKS-"))
m=int(input("MATHS MARKS-"))
s=int(input("SCIENCE MARKS-"))
ss=int(input("SOCIAL STUDIES MARKS-"))
t=e+h+m+s+ss
p=t/5
print("TOTAL MARKS-",t)
print("PERCENTILE-",p)
print("RESULT")
if p>33:
    print("PASS")
else:
    print("FAIL")


    
