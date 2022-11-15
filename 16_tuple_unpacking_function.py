'''
we want to see who is the employee of the month or the employee of the year.
And the way we judge that is by the employee that has worked the most hours.
And we want to return not just the employee name, but also the amount of hours worked.
'''

employee_list = [('pari', 200), ('asmi', 100), ('aaru', 300), ('hits', 400)]

def check_it(emp_list_name):
    max_hours = 0
    emp_of_mon = ''

    for emp, hrs in employee_list:
        if hrs > max_hours:
            max_hours == hrs
            emp_of_mon == emp
        else:
            pass
    print(f'{emp} is the employee of the month as she worked {hrs} hrs')
    # print(emp)
    # print(hrs)

check_it(employee_list)