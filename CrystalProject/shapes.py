'''
This makes a shape class with a value and fruitname
Author: Divya Subramanian
'''
class shape:
    def __init__(self, name = "?", value = 0):
        # if there is no inputted name or value, the shape will be set to a ? with value 0
        self.name = name
        self.val = value
    def __str__(self):
        # the format of the shape when printed ex. ♟: 1
        return self.name + ": " + str(self.val)
    def __eq__(self, other):
        # two shapes are equal to each other if their names and values are the same
        return self.name == other.name and self.val == other.val

def main():
    '''
    s = shape.randshape()
    print(s)
    '''
main()
