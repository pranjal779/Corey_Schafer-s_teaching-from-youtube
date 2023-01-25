class employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * employee.raise_amount)

    # classmethod decorator
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = employee("Pranjal", "Shukla", 60000)
emp_2 = employee("James", "styles", 200000)

"""
employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.05)

print(employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
"""

# Alternative constructors
emp_str_1 = 'John-Doe-1994'
emp_str_2 = 'hall-black-1989'
emp_str_3 = 'rem-dell-1999'

first, last, pay = emp_str_1.split('-')

# new_emp_1 = employee(first, last, pay)


# print(new_emp_1.email)
# print(new_emp_1.pay)
