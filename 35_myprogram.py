'''
modules - it's really just a py script, so it's a fancy way of saying, here's the py script that I'm using in another py script.

So that act of using it in another py script allows you to call it a module.

Again, this is really just semantics, but packages are then a collection of modules.

However, there's a key py script called __init__.py that needs to be placed inside of a folder to let Python know that this collection of py scripts should be treated as an entire package.
'''

from mymodule import myfunc

myfunc() # we were able to successfully call the other function from the other mymodule.py file into myprogram.py And this is the very basic way of how you would actually format the py scripts in order to not have everything in a single script.

'''
So here we can get the idea that if you have a really large script, you're not going to put everything in one giant py file.

Instead, it will be nice to split it up between multiple py files, which means you split it up between different modules.

And then later we'll see how we can aggregate a bunch of modules to create a package.
'''


from my_main_package import some_main_script

some_main_script.main_report()

from my_main_package.sub_package import some_sub_script

some_sub_script.sub_report()
