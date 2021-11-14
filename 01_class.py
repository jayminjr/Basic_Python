class Myclass():
    fname = "Jaymin"
    lname = "Patel"

    def showName(self):
        print(f"Your full name is {self.fname} {self.lname}")


clobj = Myclass()
clobj.showName()

clobj.fname = "New FirstName"
clobj.lname = "New LastName"

clobj.showName()

print(clobj)
print(type(clobj))
