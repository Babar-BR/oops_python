class Dog:
    def swim(self):
        print('dog can swim')
    def sound(self):
        print('dog sound')
class Cat:
    def swim(self):
        print('cat can swim')
    def sound(self):
        print('cat can sound')
def call(obj):
    obj.swim()
    obj.sound()
d=Dog()
c=Cat()
call(d)
call(c)
