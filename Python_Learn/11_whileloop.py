i = 1
"""
while i<35:
    print(i,end=" ")
    i=i+1
"""
"""while (True):
    if i < 5:
        i = i + 1
        continue
    print(i, end=" ")
    if i > 35:
        break
    i = i + 1
"""
"""
print("Enter your input :")
inp=int(input())

while inp<100:
    print("Re-Enter your input :")
    inp = int(input())
    if inp>100:
        print("You break the loop")
        break
"""

while True:
    inp1=int(input("Enter your number :"))
    if inp1<100:
        print("you did not break")
        continue
    else:
        print("You break loops")
        break

