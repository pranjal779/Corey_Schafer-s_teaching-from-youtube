class employees:
    # num_of_emps = 0
    # raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # employees.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * employees.raise_amount)

    def __repr__(self) -> str:
        return "Employees('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = employees("Pranjal", "Shukla", 60000)
emp_2 = employees("James", "styles", 200000)

# print(1 + 2)
# print('a' + 'b')

# print(emp_1)  # for __repr__ it returns a string now

# Dunder repr method
print("testing out the repr method: ", repr(emp_1))

# Dunder string(str) method
print("testing out the str method: ", str(emp_1))

# Test 2
print("Test2 for __repr__:", emp_1.__repr__())

print("Test2 for __str__:", emp_1.__str__())

"""
# this access dunder add
print(1+2)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
"""

# shows combined pay together
print("Combined Salaries: ", emp_1 + emp_2)

# chk Emulating numeric types docs
print("\n")
print(len('test'))

print('test'.__len__())


# Testing out the Dunder __len__ method
print("Testfor Dunder __len__: ", len(emp_1))
