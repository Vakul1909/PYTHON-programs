p=input("ENTER PASSWORD=")
n=len(p)
digit=False
special=False
upper=False
for ch in p:
    if ch.isdigit():
        digit=False
    elif not ch.isalnum():
        special=False
if p[0].isupper():
    upper=False
if digit==True and special==True and upper==True and n>=8:
    print("PASSWORD IS GOOD")
else:
    print("PASSWORD IS BAD")
        
