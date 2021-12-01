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

class Developer(Employee):
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())                                    


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

dev1 = Developer('Tejas','Nagvekar', 150000, 'python')
dev2 = Developer('Magnus','Carlsen', 150000, 'chess')
print(dev1.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev1])
print(mgr_1.email)
mgr_1.add_emp(dev2)
print(mgr_1.print_emps())

print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))