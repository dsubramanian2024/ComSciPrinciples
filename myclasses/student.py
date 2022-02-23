'''
This makes a shape class with a value and fruitname
Author: Divya Subramanian
'''
def formNum(student):
        if (student.form == 'III'):
            x = 3
        if (student.form == 'IV'):
            x = 4
        if (student.form == 'V'):
            x = 5
        if (student.form == 'VI'):
            x = 6
        return x

class student:
    def __init__(self, name = "John Smith", form = "III", grades = [98, 93, 100, 89]):
        self.name = name
        self.form = form
        self.grades = grades
    def __str__(self):
        return self.name + ", " + self.form + ", " + str(self.grades)
    def __eq__(self, other):
        return self.name == other.name and self.form == other.form and self.grades == other.grades
    def __lt__(self, other):
        x = formNum(self)
        y = formNum(other)
        return x < y
    def __gt__(self, other):
        x = formNum(self)
        y = formNum(other)
        return x > y

def main():
   s1 = student()
   print(s1)  # John Smith, III, [98, 93, 100, 89]
   s2 = student(name = "Adam B")
   print(s2) # Adam B, III, [98, 93, 100, 89]
   s3 = student(form = "IV")
   print(s3) # John Smith, IV, [98, 93, 100, 89]
   s4 = student(grades = [0, 0, 0, 0])
   print(s4) # John Smith, III, [0, 0, 0, 0]
   s5 = student("Jane Doe", "V", [100, 100, 99, 90])
   print(s5) # Jane Doe, V, [100, 100, 99, 90]
   s6 = student("Jane Doe", "V", [100, 100, 99, 90])
   print(s5 == s6) #True
   print(s1 < s4)  #False
   print(s2 > s3)  #False

main()
