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

#
# emp_1 = Employee("Sayem", "Mohammad", 20000)
# emp_2 = Employee('Test', 'User', 32000)
#
# print(emp_1.fullname())
# print(emp_1.email)
#
# print(emp_2.fullname())
# print(emp_2.email)
#
# print(emp_1.pay)
# emp_1.pay_arise()
# print(emp_1.pay)
#
# print(emp_1.__dict__)
# print(Employee.__dict__)
#
# emp_1.raise_amount = 1.025
#
# print(emp_1.__dict__)
# # print(emp_1)
# # print(emp_2)
# #
# # emp_1.first_name = 'Sayem'
# # emp_1.last_name  = 'Mohammad'
# # emp_1.email = 'sayem.mohammmad@company.com'
#
# print(Employee.num_of_employee)
#
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)

emp_1_string = 'Sayem-Mohammad-40000'
# emp_2_string = 'Test-User-32000'

# first, last, pay = emp_1_string.split('-')
# emp_1 = Employee(first, last, pay)

emp_1 = Employee.from_string(emp_1_string)

# print(emp_1.email)

import datetime
my_date = datetime.date(2017, 9, 9)

print(Employee.is_workday(my_date))