class Student():
    def __init__(self, name, std):
        self.name = name
        self.std = std
        print("This is student class constructor")

    def showdetails(self, ext):
        print("This is show details method")
        print(f"Name is {self.name} and Std is {self.std}")
        print(f"{ext} is extra parameter of showdetails method")


std1 = Student('Jaymin', 12)
std1.showdetails(1000)
print(std1.name)

std2 = Student('Pratik', 10)
std2.showdetails(2000)
