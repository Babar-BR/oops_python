#Python does not support traditional method overloading like Java.
class Demo:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c=0):
        print(a+b+c)
ob=Demo()
ob.add(2,3)
#------------------------------------------------
#We can achieve similar behavior using default arguments, *args, or type-based dispatch.

class Calculator:
    def add(self, *args):
        print(sum(args))

c = Calculator()

c.add(10, 20)
c.add(10, 20, 30)
c.add(10, 20, 30, 40)