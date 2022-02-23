'''
Divya Subramanian
A person class with first name, last name, and age as attributes
'''

class person:
    def __init__(self, fn = "Bob", ln = "Smith", age = "0"):
        self.fn = fn
        self.ln = ln
        self.age = age

    def __str__(self):
        return self.ln + ", " + self.fn + " (" + str(self.age) + ")"

class student(person):
    #pass
    # overriding init (constructor)
    def __init__(self, f, l, a, s_id = "00000"):
        super().__init__(f, l, a)
        self.id = s_id

    def __str__(self):
        return super().__str__() + " | " + str(self.id)

class teacher(person):
    #pass
    def __init__(self, f, l, a, dept = "math"):
        super().__init__(f, l, a)
        self.dept = dept

    def __str__(self):
        return super().__str__() + " | " + str(self.dept)

class admin(person):
    #pass
    def __init__(self, f, l, a, div = "administration"):
        super().__init__(f, l, a)
        self.div = div

    def __str__(self):
        return super().__str__() + " | " + str(self.div)

class parent(person):
    #pass
    def __init__(self, f, l, a, childname = "Bob Smith"):
        super().__init__(f, l, a)
        self.cn = childname

    def __str__(self):
        return super().__str__() + " | " + self.cn


def main():
    p = person()
    print(p)
    ad = admin("Divya", "Subramanian", 45)
    print(ad)

main()
