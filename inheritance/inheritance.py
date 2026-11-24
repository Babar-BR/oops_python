class Human:
    def __init__(self,n):
        self.n=n
    def start(self):
        print('hi i am human')
    def work(self):
            print('hi i am work')
class Male(Human):
    def __init__(self,n):
        self.n=n
    
class Female(Male,Human):
    def __init__(self,n):
        self.n=n
    def  beauty(self):
        print('i am girl')
        
        
ob=Female(2)
ob.work()
