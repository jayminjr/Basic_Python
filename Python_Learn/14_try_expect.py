print("ENter 1 number :")
num1=input()
print("ENter 2 number :")
num2=input()
try:
    print("Sum of two number is :",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is very important line...")