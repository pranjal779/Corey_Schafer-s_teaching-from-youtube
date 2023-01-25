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
        # or
        # self.pay = int(self.pay * self.raise_amount)
        # any of the two above works
        # self.pay = int(self.pay * 1.04) -> is a very hardcoded value


# checking the numbers of employees at the start.
print(employee.num_of_emps)

emp_1 = employee("Pranjal", "Shukla", 60000)
emp_2 = employee("James", "styles", 200000)

"""
# for line 19
print("without pay raise: ", emp_1)

# with pay raise for line 19
emp_1.apply_raise()
print("with pay raise: ", emp_1)
"""
# emp_1.raise_amount
# employee.raise_amount

# for raise_amount:
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# employee dict
# print(employee.dict)

# employee.raise_amount = 1.05
emp_1.raise_amount = 1.05

print(emp_1.__dict__)

# for raise_amount:
print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# number of employees
print(employee.num_of_emps)
