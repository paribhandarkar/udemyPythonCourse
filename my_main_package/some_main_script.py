def main_report():
    print("hey im in main report inside main package")

'''
since these are just directories or folders, we need to let Python be able to understand that we want to treat these directories not just as a normal directory but as an actual package.

So to do that inside both my main package and sub package, I'm going to have to create, a file called __init__.py

you don't actually need to write anything in this file. It just needs to be there so that when Python goes searching through these packages, it understands that it's not just a normal directory, it's an actual package.
'''