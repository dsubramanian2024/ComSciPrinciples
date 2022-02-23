'''
Point and Triangle Class
Divya, Mirika, and Kyra
This program creates points and allows the user to perform a variety of functions with those points
Additionally, users can create a triangle and test other functions such as congruence
'''
import random
import math

class point:
    namearray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    instance = 0 #creating a list with all possible names; instance is used to make sure that the amount of points does not go over 26 points

    def exceed_point():
        if (point.instance > 26): #if the number of points has exceeded 26 points, then it will print a statement saying so
            print("You have exceeded the amount of points")
            exit()

    def __init__(self, x = 0, y = 0):
        self.x = x #initializing and overloading the variables
        self.y = y
        point.instance += 1 #every time a new point is created, 1 is added to instance
        point.exceed_point() #calling the exceed point function to make sure the number of points is less than 26
        self.name = point.namearray[point.instance - 1] #assigns the name based on the index from list names, and using instance to figure out which index

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

class triangle:
    def __init__(self, p1 = point(0, 1), p2 = point(1, 0), p3 = point(1, 1)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3 #sets three points
        self.name = self.p1.name + self.p2.name + self.p3.name #creates a triangle name by combining the point names

    def __str__(self):
        return self.name #returns the name

    def perimeter(self):
        return math.sqrt((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p1.y)**2) + math.sqrt((self.p3.x - self.p1.x)**2 + (self.p3.y - self.p1.y)**2) + math.sqrt((self.p3.x - self.p1.x)**2 + (self.p3.y - self.p1.y)**2)
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

def main():

    a = 3
    s = str("abc")
    print(s)
    '''
    # . is dot operator
    p = point()
    print(p.name) # prints A
    print(p) # prints location/memory address
    for i in range(0,27):
        p = point(0,0)
        print(point.instance)
    '''
    p1 = point(1,3)
    p2 = point(2,4)
    print(p1)
    print(p2)
    print(point.slope2(p1, p2))
    print(point.distance2(p1, p2))
    print(p1==p2)
    tri = triangle()
    print(tri.area())
    print(tri.name)
    print(tri.perimeter())
    tri2 = triangle.randTriangle()
    print(tri2)
    triangle.printpoints(tri2)
    print(tri2.area())
    print(tri2.perimeter())
    tri3 = triangle(point(2, 1), point(1, 2), point(2, 2))
    tri4 = triangle(point(2, 1), point(1, 2), point(2, 2))
    print(triangle.congruentTo(tri2, tri3))
    print(triangle.congruentTo(tri3, tri4))







main()
