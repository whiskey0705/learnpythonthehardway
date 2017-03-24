class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        self.name = name



class Person(object):
    
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog('Rover')
print(rover.name)

satan = Cat('Satan')
print(satan.name)

mary = Person('mary')
mary.pet = satan
print(f'{mary.name} has a cat named {mary.pet.name}')


frank = Employee('Frank', 12000)
frank.pet = rover
print(f'{frank.name} makes {frank.salary}/month, and has a dog named {frank.pet.name}')

