"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+" adındaki PErsonel"
p1=Person("John",36)
print(p1.name)
print(p1.age)
print(p1)

"""




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname,bolum):
    Person.__init__(self,fname,lname) #super().__init__(fname,lname)
    self.bolum=bolum


x=Student("mike","olsen","ybs")
x.printname()
print(x.bolum)



