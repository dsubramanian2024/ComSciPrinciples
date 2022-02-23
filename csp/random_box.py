'''
Generates a random box
Author: Mirika and Divya
'''

from myclasses.box import box #box is the name of the class
import sys # to get command line arguements
import random

def generate_random_box():
    # randomly chooses values from 1 to 10 for x, y, and x values
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    return box(x, y, z)

def get_name():
    # asks the user and returns a name for the box
    userinput = input("Please enter a name for our random box: ")
    return userinput

def choose_func(p):
    # checks the command line arh=guements. if one is inputted, volume is calculated. Otherwise, surface area is calculated
    if len(sys.argv) > 1 and sys.argv[1] == "1":
        print("Calculates Volume")
        return p.volume()
    else:
        print("Calculates Surface Area")
        return p.surface_area()

def callfunc():
    # calls the functions to get name, box, and function of box
    randbox = generate_random_box()
    name = get_name()
    randbox.name =  name
    print(randbox)
    print(choose_func(randbox))

callfunc()
