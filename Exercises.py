print("Welcome to the calculator")
print("1.ADDITION")
print("2.MULTIPLICATION")
print("3.SUBTRATCTIO")
print("4.DIVISION")

operation=input()
if operation=="1":
    num1=input("Enter first number")
    num2=input("Enter second number")
    print("The sum is" + str(int(num1)+int(num2)))