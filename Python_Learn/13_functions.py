a = 8
b = 9
print(sum((a, b)))


def function1():
    print("You are in function")

function1()

def sumfunction(a,b):
    print("Sum of number is :",a+b)

sumfunction(5,5)

def averagefunction(x,y):
    """This function give average of two numbers"""
    average=(x+y)/2
    return average

print(averagefunction.__doc__)
ans=averagefunction(12,12)
print(ans)