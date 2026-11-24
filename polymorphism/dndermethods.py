class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} and {self.age}'
    def __add__(self, other):
        return a+b
    def __call__(self, *args, **kwds):
        print('hi bro i am dunder')
            
obj=A('babar',23)
print(2,4)
print(obj)
obj()