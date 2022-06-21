class Company:
    pass

class Employee(Company):

    raise_amount = 1.04 #Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Peter', 'Ross', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
    