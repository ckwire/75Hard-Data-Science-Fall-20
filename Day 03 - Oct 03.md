## OCTOBER 3nd 2020 - DAY 3 - DAILY LOG ##

* Finding Purpose
    Sometimes it is good to make sure you have defined the goals and meeting them. This challenge so far has been my end of day routine and is getting neglected.

    The progress made so far is lacking any real progress just checking the box for the day from my README.md. 


* Classes 
    * Refreshing class syntax for Python and actually learning today! 

    ```python
    #allows for middle name arg to be ignored
    def get_formatted_name(first_name, last_name, middle_name=''):
        if middle_name:
            full_name = first_name + ' ' + middle_name + ' ' + last_name
        else:
            full_name = first_name + ' ' + last_name
        return full_name.title()

    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)

    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)
    ```


* reference: [Corey Schafer - Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=580s)

