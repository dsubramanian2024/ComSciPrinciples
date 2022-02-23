'''
Author: Divya Subramanian
This code creates different classes and dispays has a and is a relationships.
'''

import random
import math

class point:
    #namearray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    #instance = 0 #creating a list with all possible names; instance is used to make sure that the amount of points does not go over 26 points

    def exceed_point():
        if (point.instance > 26): #if the number of points has exceeded 26 points, then it will print a statement saying so
            print("You have exceeded the amount of points")
            exit()

    def __init__(self, x = 0, y = 0, name = 'A'):
        self.x = x #initializing and overloading the variables
        self.y = y
        #point.instance += 1 #every time a new point is created, 1 is added to instance
        self.name = name
        #point.exceed_point() #calling the exceed point function to make sure the number of points is less than 26
        #self.name = point.namearray[point.instance - 1] #assigns the name based on the index from list names, and using instance to figure out which index

    def __str__(self):
        # returns in form of name(x,y)
        return self.name + "(" + str(self.x) + ", " + str(self.y) + ")"
        #returns the point name and coordinates

    def distance1(self, other):
        #finds the distance from one point to another
        return math.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))

    def slope1(self, other):
        #finds the slope of the side
        return (self.y - other.y)/(self.x - other.x)

    def distance2(a, b):
        #static method for distance, taking in the two points
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def slope2(a, b):
        #static method for slope
        return (a.y - b.y)/(a.x - b.x)

    def __eq__(self, other):
        #checks if sides are equal
        return self.x == other.x and self.y == other.y


class polygon:
    #super or base class
    def __init__(self, num_of_side = 3):
        self.num_of_side = num_of_side

    def area(self):
        pass #cannot calculate area, needs to be more specific

    def about(self):
        print("This is a 2-D shape.")

    def perimeter(self):
        pass #cannot calculate perimeter, needs to be more specific

    def __str__(self):
        return "number of sides: " + str(self.num_of_side)


class triangle(polygon):
    def __init__(self, p1 = point(0, 1, 'A'), p2 = point(1, 0, 'B'), p3 = point(1, 1, 'C')):
        super().__init__(3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3 #sets three points
        self.name = self.p1.name + self.p2.name + self.p3.name #creates a triangle name by combining the point names, could be done if points were not inputter

    def __str__(self):
        return super().__str__() + " | " + str(self.name)#returns the name

    def perimeter(self):
        return point.distance1(self.p1, self.p2) + point.distance1(self.p2, self.p3) + point.distance1(self.p3, self.p1)
        #the distances are found of all three sides, and then added together

    def area(self):
        a = point.distance1(self.p1, self.p2) #sets distance from point 1 to point 2
        b = point.distance1(self.p2, self.p3) #sets distance from point 2 to point 3
        c = point.distance1(self.p3, self.p1) #sets distance from point 3 to point 1
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c)) #using heron's formula to calculate the area

    def congruentTo(self, other):
        a1 = point.distance1(self.p1, self.p2) #sets distance from point 1 to point 2
        b1 = point.distance1(self.p2, self.p3) #sets distance from point 2 to point 3
        c1 = point.distance1(self.p3, self.p1) #sets distance from point 3 to point 1
        a2 = point.distance1(other.p1, other.p2) #sets distance from point 1 to point 2
        b2 = point.distance1(other.p2, other.p3) #sets distance from point 2 to point 3
        c2 = point.distance1(other.p3, other.p1) #sets distance from point 3 to point 1
        return a1 == a2 and b1 == b2 and c1 == c2 #checks if all sides of both triangles are equal

    def randTriangle():
        return triangle(p1 = point(random.randint(0, 25), random.randint(0, 25)), p2 = point(random.randint(0, 25), random.randint(0, 25)), p3 = point(random.randint(0, 25), random.randint(0, 25)))
        #creates a random triangle

    def printpoints(self):
        print("p1: (" + str(self.p1.x) + ", " + str(self.p1.y) + ")  " + "p2: (" + str(self.p2.x) + ", " + str(self.p2.y) + ")" + "p3: (" + str(self.p3.x) + ", " + str(self.p3.y) + ")")
        #prints the points of the triangle

    def about(self):
        print("This is a 2D shape that has 3 sides")

class rectangle(polygon):
    def __init__(self, p1 = point(0, 0, 'A'), p2 = point(0, 1, 'B'), p3 = point(1, 1, 'C'), p4 = point(1, 0, 'D')):#assuming that the points are in the right order
        super().__init__(4) #num of sides is 4
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.name = self.p1.name + self.p2.name + self.p3.name + self.p4.name#creates a rectangle name by combining the point names but this only works if points are not inputted

    def __str__(self):
        return super().__str__() + " | " + str(self.name) #returns the name

    def area(self):
        a = point.distance1(self.p1, self.p2) #sets distance from point 1 to point 2
        b = point.distance1(self.p2, self.p3) #sets distance from point 2 to point 3
        return a * b

    def perimeter(self):
        a = point.distance1(self.p1, self.p2) #sets distance from point 1 to point 2
        b = point.distance1(self.p2, self.p3) #sets distance from point 2 to point 3
        return (2 * a) + (2 * b)

    def about(self):
        print("This is a 2D shape that has 4 sides")

class square(rectangle): #has a is a relationship with rectangle
    def __init__(self, p1 = point(0, 0, 'A'), p2 = point(0, 1, 'B'), p3 = point(1, 1, 'C'), p4 = point(1, 0, 'D')):#assuming that the points are in the right order
        super().__init__(p1, p2, p3, p4) # inherits everything from rectangle

    def __str__(self):
        return super().__str__() + " | square" #returns the name

def main():
    s1 = square()
    print(s1)
    print(s1.perimeter())
    print(s1.area())
    s1.about()
    p1 = point(0, 4)
    p2 = point(0, 0, 'B')
    p3 = point(3, 0, 'C')
    tri = triangle(p1, p2, p3)
    print(tri)
    print(tri.perimeter())
    print(tri.area())
    tri.about()
main()
