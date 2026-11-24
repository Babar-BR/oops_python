class A:
    def add(self,a,b):
        print(f'i am from parent {a+b}')

class B(A): 
    def add(self,a,b):
        super().add(a,b)
        print(f'i am child {a+b}')
ob=B()
ob.add(2,3)