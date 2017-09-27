class Employee:
    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self,first,last,pay):
        '''
        Termed as constructor in other language.
        Initialization in python.
        It will run automatically after a class called.

        :param first: First Name.
        :param last: Last Name.
        :param pay: Payment.
        '''

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def pay_arise(self):
        self.pay =  int(self.pay + self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        '''
        This Method is called class Method. This is used for class. And here 'cls' parameter is used for getting class
        into method. To define a class method we have to give '@classmethod' above the function.
        '''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        '''
        This function will take a string input to classs.
        :param emp_str:
        :return:
        '''
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        '''
        Its a static method. It won't take any parameter like class or instance. It has a logical connection between
        class.
        Python has a built in function called "weekday()" which can detect the day as number. In this function count
        starts from "Monday" & count start from 0.

        :param day: Takes input as day
        :return: return true if its a workday.
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Devoloper(Employee):
    raise_amount = 1.10  # It will override the value of Employee inheritanted. But it will not change any value of the
                          # class varriable in Employee class.

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return "Devoloper('{}', '{}', {}, '{}')".format(self.first, self.last, self.pay, self.prog_lang)

    def __add__(self,other):
        return self.pay + other.pay


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--> ', emp.fullname())

    def __repr__(self):
        '''
        If there is double underscope before a function then it can be read as "DUNDER FUNCTION NAME ".

        This function will make the object viewing user friendly.
        '''
        return "Employee('{}', '{}', {}, {})".format(self.first, self.last, self.pay, self.employees)

    def __str__(self):
        '''
        If there is __str__(string) method there it will run first if the object is been told to  print outside the
        class.
        These functions are called "Magic Function".
        '''
        return "{} --> {}".format(self.fullname(), self.email)


dev_1 = Devoloper('Sayem', 'Mohammad', 20000, 'Python')
dev_2 = Devoloper('Test', 'User', 32000, 'Java')
print(dev_1.email)
print(dev_1.prog_lang)

# This line will print everything associated with this class.
# print(help(Devoloper))

# print(dev_1.pay)
# dev_1.pay_arise()
# print(dev_1.pay)

mngr_1 = Manager('Sue', 'Young', 90000, [dev_1])
print(mngr_1.email)
# mngr_1.print_emp()

mngr_1.add_employee(dev_2)
mngr_1.remove_employee(dev_1)

mngr_1.print_emp()

# There is built in function in python called "issubclass" which tell us if the class is sub class of other one.
print(issubclass(Manager, Employee))

# There is another built in class called "isinstance" which will allow us to verify if that object instance from
# that class.
print(isinstance(mngr_1, Employee))

# In this print function it will call __str__ function & will represent the class more user friendly. If there is no
# __str__ function it will print the __repr__ function. These methods are called MAGIC FUNCTION.
print(mngr_1)

print('-' * 50)

# -->> showing How addition and concadition works in python
print(int.__add__(1, 2))
print(str.__add__('a', 'n'))

print('-' * 50)

# Printing the wages of two devoloper
print(dev_1 + dev_2)