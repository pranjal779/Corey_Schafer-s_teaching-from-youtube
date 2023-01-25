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


# Creating subclasses
class Developers(employees):
    raise_amt = 1.10

    def __init__(self, first, last, pay, programming_lang):
        # super does not have self as arg.
        super().__init__(first, last, pay)
        # employee.__init__(self, first, last, pay) also works but super() is much more maintainable.
        self.programming_lang = programming_lang


class Manager(employees):

    def __init__(self, first, last, pay, employeesz=None):
        super().__init__(first, last, pay)
        if employeesz is None:
            self.employeesz = []
        else:
            self.employeesz = employeesz

    def add_emp(self, emp):
        if emp not in self.employeesz:
            self.employeesz.append(emp)

    def remove_emp(self, emp):
        if emp in self.employeesz:
            self.employeesz.remove(emp)

    def print_emps(self):
        for emp in self.employeesz:
            print(' --->', emp.fullname())


# emp_1 = employees("Pranjal", "Shukla", 60000)
dev_1 = Developers("Pranjal", "Shukla", 60000, 'Python')
dev_2 = Developers("James", "styles", 200000, 'Java')

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developers))

"""
output for Developers class
"""
# print("Devs email: ", dev_1.email)
# print("Devs programming language: ", dev_1.programming_lang)

"""
output for Manager class
"""
mngr_1 = Manager("Luffy", "D_Monkey", 350000, [dev_1])

print("Luffy the Manager's email is: ", mngr_1.email)
# print(mngr_1.print_emps)
print("employees under Luffy the Manager: ", mngr_1.print_emps())

mngr_1.add_emp(dev_2)

# print("employees under Luffy the Manager: ", mngr_1.print_emps())

mngr_1.print_emps()


# mngr_1.remove_emp(dev_1)


# print(dev_1.pay)

# dev_1.apply_raise()
# print("After pay raise:", dev_1.pay)


"""
isinstance & issubclass
"""

# is a instance of manager
print("\nis a instance of manager:", isinstance(mngr_1, Manager))

# is a instance of employees
print("\nis a instance of employees:", isinstance(mngr_1, employees))

# is a instance of Developer
print("\nis a instance of Developer:", isinstance(mngr_1, Developers))

# is a subclass of employees
print("\nis a subclass of employees:", issubclass(Developers, employees))

# is a isinstance of employees
print("\nis a isinstance of employees:", isinstance(Developers, employees))


# Manager is a subclass of employees
print("\nis a subclass of employees:", issubclass(Manager, employees))

# Manager is a subclass of Developers
print("\nis a subclass of employees:", issubclass(Manager, Developers))
