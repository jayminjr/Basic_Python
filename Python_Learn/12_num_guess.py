n=28

while True:
    n1=int(input("Enter number :"))
    if n1>n:
        print("You entered bigger")
        continue
    elif n1<n:
        print("You entered smaller")
        continue
    else:
        print("You got it")
        break