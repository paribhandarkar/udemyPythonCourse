'''
As you begin to expand to larger multi file projects or you begin to work with a team that's bigger than just yourself, it becomes really important to have tests in place as you or your teammates make changes or update your code.

You can run your test files to make sure previous code still runs as expected. There are several testing tools and we're going to focus on two: pylint and unit testing

pylint: this is a library that in general looks at your code and reports back possible issues. Maybe you have styling issues or maybe you have some invalid code and it will report back issues of your code. Python has a set of style convention rules known as "PEP 8"

unit test library: This is a built in library in Python that's going to allow you to test your own programs and then check if you're getting the desired outputs.
'''

a = 4
b = 6
print(a)
print(b)

# for running with pylint type pylint "d:\python prac\38_pylint.py"  in the terminal"
# the above code was rated 0/10

'''
what pylint does is it issues what is essentially an automated report grading your code.
it gives us raw metrics such as how much code are there, how many docs, strings are there, comments, how much is empty?
How many functions do I have in this code and are they documented? Do they have a stylized name that's inappropriate?

Sometimes to get something ten out of ten, it has to be very machine readable instead of human readable. And you always want to balance that.

this is really more for when you're working with other people or you're working with really large programs and you have kind of strict methods for yourself to make sure everything is up to some sort of style convention.
'''