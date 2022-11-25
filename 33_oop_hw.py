# Object Oriented Programming Homework Assignment

# Problem 1

'''
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
9.433981132056603
li.slope()
1.6
'''

class Line:
    
    def __init__(self,coor1,coor2):
        # self.coor1 = coor1
        # self.coor2 = coor2
        self.x_of_coor1 = coor1[0]
        self.x_of_coor2 = coor2[0]
        self.y_of_coor1 = coor1[1]
        self.y_of_coor2 = coor2[1]
    
    def distance(self):
        return ((self.x_of_coor2 - self.x_of_coor1)**2 + (self.y_of_coor2 - self.y_of_coor1)**2)**(1/2)
    
    def slope(self):
        return (self.y_of_coor2 - self.y_of_coor1)/(self.x_of_coor2 - self.x_of_coor1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

'''
u can also use tuple unpacking here

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
        
'''

# Problem 2

'''
Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass
# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
56.52
c.surface_area()
94.2
'''

class Cylinder:
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius**2)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())