from operator import mod


x = open('test.txt', 'w')
x.write('Hello World')
x.close()

# x = open('test1.txt') # If I run this, we'll get a file not found error. So this is a really common error. It's called error number two. No such file or directory.

myfile = open('D:\OneDrive\Desktop\\contact-no.txt')
print(myfile.read())
myfile.close()

with open('test.txt', mode='a') as f:
    f.write('\nadded a line haha')
with open('test.txt', mode='r') as f:
    print(f.read())
with open('new-file-with-code.txt', mode='w') as f:
    f.write('created a new file')