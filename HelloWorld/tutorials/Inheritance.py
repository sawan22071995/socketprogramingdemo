class Mammal:
    def walk(self):
        print('Walk')
class Dog(Mammal):
    def bark(self):
        print('bark')

class cat(Mammal):
    pass
dog=Dog()
dog.walk()
dog.bark()
