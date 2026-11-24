class Emp:
    class_variable_name='Sbit'
    @classmethod
    def show(cls,name):
        cls.class_variable_name=name
Emp.show('BABABR')
print(Emp.class_variable_name)