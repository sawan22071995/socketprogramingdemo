class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('speaks english!!')

person=Person('sawan')
print(f"the name of the person is {person.name}")
person.talk()