
n="a"
for i in range(0,6):
    for j in range(0,i):
        print(n,end="")
        if n.isupper():
            n=n.lower()
        else:
            n=n.upper()
        n=chr(ord(n)+1)
    print()
s1=input("enter a string")
n=len(s1)
for ch in s1:
    if ch=='a'and ch=='z':
        print(chr(ord(ch)-32),end='')
    elif ch>='A'and ch<='Z':
          print(ch,end='')
'''
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

    # take input from the user
choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        
else:
        print("Invalid Input")
'''        

        
