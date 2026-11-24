
from abstarction.abstract_class import Huuman

class Car(Huuman):
    def __init__(self,n):
        self.n=n
    def start(self):
        print('i am car')
class Bike(Huuman):
    def __init__(self,n):
        self.n=n
    def start(self):
        print('i am Bike',self.n)
