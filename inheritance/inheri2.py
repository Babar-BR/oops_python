class Human(object):
    def start(self):
        print('i am human')
class Boy(Human):
    def work(self):
        print('i can work')
class Girl(Boy):
    def beauty(self):
        print('i am so beautifull') 
ob=Girl()
print(issubclass(Boy,Human))
print(issubclass(Human,object))

 