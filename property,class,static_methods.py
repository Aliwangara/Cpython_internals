


class Employee:
    number_of_emps = 0
    raise_amount =1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.number_of_emps+=1

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount): # we have used cls in this method instead of self thats what classmethod allows us to do
        # this means that we are working with class instead of instance eg:

        cls.raise_amount =amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    #Unlike other methods which either use the instance(self) or class(cls) static method doesnt take 
    # the (cls or self)

    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

import datetime

my_date = datetime.date(2026,10,14)

print(Employee.work_day(my_date))






employee1 = Employee("Ali", "Wangara", 2000)
# print(employee1.full_name()) THIS SHOWS WE ARE USING A METHOD BUT IF WE WANT TO USE IT WITHOUT THE 
# PARENTHESIS WE CAN USE THE @property method at the top of the full_name method because it returns a string instead of a function

print(employee1.full_name) # this becomes attribute style lookup  returns a string instead of a function




# employee2 = Employee("George", "Wangara", 4000)


# Employee.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(employee1.raise_amount)
# print(employee2.raise_amount)

#SOME USE CASES FOR CLASSMETHOD. I will start with before using and after using it

#BEFORE:

# name_1 = "ALI-WANGARA-2000"

# first,last,pay = name_1.split("-")
# new_name_1 = Employee(first,last,pay)
# print(new_name_1.email)
# print(new_name_1.pay)

# AFTER. PRINTS FROM A CLASS METHOD

# emp_1 = Employee.from_string(name_1)

# print(emp_1.email)
# print(emp_1.pay)
    