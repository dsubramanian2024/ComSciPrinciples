import random

class fruit:
    array = ["apple", "banana", "pear", "cherry", "mango", "kiwi", "cherry", "orange", "pomogranate", "grapes"]
    def __init__(self, name = "apple"):
      self.name = name
    def __str__(self):
        return "fruit: " + self.name
    @classmethod
    def randfruit(cls):
        return fruit(fruit.array[random.randint(0, 9)])


class basket:
    def __init__(self, fruit1 = fruit("apple"), fruit2 = fruit("banana")):
        self.fr1 = fruit1
        self.fr2 = fruit2

    def __str__(self):
        return str(self.fr1) + " and " + str(self.fr2)P + " are in the basket."

def main():
    print(fruit.randfruit())
    print(basket(fruit("pear")))
main()
