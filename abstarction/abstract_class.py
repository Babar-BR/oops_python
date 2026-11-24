from abc import ABC ,abstractmethod
class Huuman(ABC):
    def __init__(self,n):
        self.n=n
    @abstractmethod
    def work(self):
        pass
    def display():
        print('display the method')
