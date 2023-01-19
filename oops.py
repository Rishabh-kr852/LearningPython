class Employee:
    num_of_emp = 0
    raise_amt = 1.04
    
    # Constructor
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        
        Employee.num_of_emp += 1  # class variable = Employee.num_of_emp
    
    @property   
    def email(self):                                                                        # getter
        return '{}.{}@email.com'.format(self.fname,self.lname)
    
    # Full name function   
    @property      
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @fullName.setter                                                                        #setter
    def fullName(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname
        
    @fullName.deleter
    def fullName(self):
        print('Name Deleted!')
        self.fname = None
        self.lname = None
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)           # instance varaible = self.raise_amt
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):                          # alternate constructor starts from 'from_name'
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod                                           # used to create when no instance of class is being used in function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    # Magic/Dunder methods dunder = surrounded by double underscore i.e. __a__
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.fname, self.lname, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fname, self.lname)
    
    
    # Operator overloading
    def __add__(self, other):
        return self.pay + other.pay
    
    
# INHERITANCE
class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang  

class Manager(Employee):
    
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
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
            
    def print_emp(self):
        for i in self.employees:
            print('--->',i.fullName())
    
    
    
    
    
emp1 = Employee('Dennis', 'Harrison', 1000000)
emp2 = Employee('Richie', 'Harrison', 2000000)


# print(emp1.fullName())
# print(Employee.fullName(emp1))

# emp1.raise_amt = 1.05
# Employee.set_raise_amt(1.05)
# emp1.apply_raise()
# print(emp1.pay)

# emp_str_1 = 'Hello-World-404'
# new_emp = Employee.from_string(emp_str_1)
# print(new_emp.fullName())

# import datetime
# my_date = datetime.date(2022,12,19)
# print(Employee.is_workday(my_date))

dev1 = Developer('Hello', 'World', 50000, 'C++')
# print(dev1.fullName())

mgr1 = Manager('Angela', 'Yu', 10000, [dev1])
# mgr1.print_emp()
dev2 = Developer('Harry', 'styles', 50000, 'Java')

mgr1.add_emp(dev2)

mgr1.remove_emp(dev1)
# mgr1.print_emp()

# print(isinstance(mgr1, Employee))
# print(isinstance(mgr1, Developer))
# print(issubclass(Manager, Employee))
# print(isinstance(Developer, Manager))

emp1.fullName = 'Emma Mayers'

del emp1.fullName
print(emp1.fullName)