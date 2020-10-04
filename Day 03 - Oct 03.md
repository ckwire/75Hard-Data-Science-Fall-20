## OCTOBER 3nd 2020 - DAY 3 - DAILY LOG ##

* Finding Purpose
    Sometimes it is good to make sure you have defined the goals and meeting them. This challenge so far has been my end of day routine and is getting neglected.

    The progress made so far is lacking any real progress just checking the box for the day from my README.md. 


* Classes 
    * Refreshing class syntax for Python and actually learning today! 

    ```python
    #it is possible when I copy this from my working file to this code section the formatting will all adjust to the left. Technically cause an error with the class and method definitions.
   class Employee:

        raise_amount = 1.04
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@email.com'

        def fullname(self):
            return '{} {}'.format(self.first, self.last)
            #using '{}'.format(var) is a newer syntax to me - allows good to check Python docs to learn more!

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)


    emp_1 = Employee('Johnny', 'Appleseed', 50000)
    emp_2 = Employee('Bob', 'Roberts', 72500)

    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)
    ```

* Random tidbits
    Learning to copy line down/up in VS Code


* reference: 
    * [Corey Schafer - Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=580s)
    * [Python.org Advance Str Formatting](https://www.python.org/dev/peps/pep-3101/)


