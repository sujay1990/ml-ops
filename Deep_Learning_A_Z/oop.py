# Python object oriented programming

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        pass

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True        


print(Employee.num_of_employees)
emp1 = Employee('Sujay','Nagvekar', 150000)      
emp2 = Employee('Shradha','Nagvekar', 150000)    
print(emp1.email)
print(emp2.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.num_of_employees)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
emp1.apply_raise()
print(emp1.pay)

import datetime
my_date = datetime.date(2016,7,11)

print(Employee.is_work_day(my_date))