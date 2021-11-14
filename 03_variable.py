class Student():
    clvar = "This is class variable"  # this is class variable

    def __init__(self, name, std):  # this is instance method
        self.name = name  # this is instance variable
        self.std = std  # this is instance variable
        print("This is student class constructor")

    def showdetails(self):
        print("This is show details method")
        print(f"Name is {self.name} and Std is {self.std}")


std1 = Student('Jaymin', 12)
std1.showdetails()
print(std1.name)  # accessing instance variable outside class
print(Student.clvar)  # accessing class variable outside class
Student.clvar = "Change clvar"  # change class variable value
print(Student.clvar)
