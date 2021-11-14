list1 = [["jaymin", 10], ["niriksha", 20], ["papa", 30], ["mummy",40]]

print(type(list1))
print(list1)

for item, income in list1:
    # print(item)
    print(item, "and income is", income)
#quiz quick
list2=[1,4,5,6,8,9,10,12]
print(type(list2))
print("Print Full list",list2)
for item in list2:
    if item>=6:
        print(item)