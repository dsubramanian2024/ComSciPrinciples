'''

Authors: Mirika and Divya

This is a function that takes in the characteristics of a box
and calculates the volume and surface area

'''

import random
class box:
    def __init__(self, a = 0, b = 0, c = 0, n = "A"): #attributes or classfields - length, width, height, and name
        self.x = a
        self.y = b
        self.z = c
        self.name = n

    def __str__(self):
        #prints attributes if used with print function
        return self.name + "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def volume(self):
        # calculates the volume of the box by multiplying the x, y, and z values of the box
        return(self.x * self.y * self.z)

    def __GT__(self, other)
        if (self.x * self.y * self.x) is > (other.x * other.y * other.z)

    def __LT__(self, other):
        if (self.volume() > other.volume()):
            return other
        else:
            return self

    def surface_area(self):
        return((self.x * self.y * 2) + (self.y * self.z * 2) + (self.x * self.z * 2))
        # calculates the surface area of the box, using the x, y, and z values of the box

    def __eq__(self, other):
        # checks to see if the x, y, and z values are the same
        return self.x == other.x and self.y == other.y and self.z == other.z

    def randbox():
        return box(random.randint(0,10), random.randint(0,10), random.randint(0,10))

def main():
    '''
    p = box(3, 4, 5, "CoolBox")
    print(p)
    print("Volume:")
    print (p.volume())
    print("Surface Area")
    print (p.surface_area())
'''

main()
