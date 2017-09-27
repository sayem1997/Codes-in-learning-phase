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

        Employee.num_of_employee += 1

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted!')
        self.first = None
        self.last = None

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

emp_1 = Employee('John', "Ghomez", 52000)

emp_1.fullname = "Sayem Mohammad"

print(emp_1.email)
del emp_1.fullname