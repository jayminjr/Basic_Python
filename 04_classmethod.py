class Student():
    clvar = "This is class variable"

    @classmethod
    def clmethod(cls, nvar):
        cls.clvar = nvar


print(Student.clvar)
Student.clmethod("change value of class variable using class method")
print(Student.clvar)
