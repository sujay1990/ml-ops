# Python object oriented programming

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Sujay','Nagvekar', 150000)      
emp2 = Employee('Shradha','Nagvekar', 150000)    
print(emp1.email)
print(emp2.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)