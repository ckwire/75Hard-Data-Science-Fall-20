## OCTOBER 4th 2020 - DAY 4 - DAILY LOG ##

* What to do today?

* Classes (cont)

    ```python
    #it is possible when I copy this from my working file to this code section the formatting will all adjust to the left. Technically cause an error with the class and method definitions.
   class Employee:

        num_of_emps = 0
        raise_amt = 1.04
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@email.com'

            Employee.num_of_emps += 1

        def fullname(self):
            return '{} {}'.format(self.first, self.last)
            #using '{}'.format(var) is a newer syntax to me - allows good to check Python docs to learn more!

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)

        @classmethod
        def set_raise_amt(cls, amount):
            cls.raise_amt = amount


    emp_1 = Employee('Johnny', 'Appleseed', 50000)
    emp_2 = Employee('Bob', 'Roberts', 72500)

    Employee.set_raise_amt(1.08)

    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    ```



* reference: 
    * [Corey Schafer - Python OOP Tutorial(s)](https://www.youtube.com/watch?v=BJ-VvGyQxho&t=305s)


