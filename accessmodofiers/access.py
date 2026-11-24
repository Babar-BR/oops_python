
# 1. Public
# 2. Protected
# 3. Private
# Let's understand each with simple examples.

#public
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Babar")

print(s.name)
#Protected access modifier
class Student:
    def __init__(self, name):
        self._name = name

class Child(Student):
    def display(self):
        print(self._name)

s = Child("Babar")
s.display()
#Private access modifier
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print(self.__age)

s = Student("Babar", 22)

s.display()