class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = employee("Pranjal", "Shukla", 60000)
emp_2 = employee("James", "styles", 200000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))

print("using the fullname def:")
print(emp_1.fullname())


# compare
print("look at these 2:")

print("emp_1.fullname: ", emp_1.fullname())
print("employee.fullname(emp_1):", employee.fullname(emp_1))

emp_2.fullname()
