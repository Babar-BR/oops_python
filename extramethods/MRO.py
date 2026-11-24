class Father:
    def start(self):
        print('i am father')
class Mother:
    def start(self):
        print('i am from mother')
class Child(Father,Mother):
    def start(self):
        print('i am child')
ob=Child()
print(Child.mro())