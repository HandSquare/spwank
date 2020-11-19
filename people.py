"""
Define characters
"""

class Person(object):

    def _init_(self, name):
        self.inventory = {}
        self.health = 100
        self.insight = 0
        self.alive = None
        self.name = name
        self.blood_of_the_tribe = 0.0
    
    def spawn(self):
        self.alive = True

    def die(self):
        self.alive = False
        

class Brian(person):
    def __init__(self):
        Person.__init__(self, name = 'Brian')
        self.blood_of_the_tribe = self.blood_of_the_tribe
        
class Caleb(person):
    def __init__(self):
        Person.__init__(self, name = 'Caleb')
        self.blood_of_the_tribe = self.blood_of_the_tribe + 0.50            


class Gio(person):
    def __init__(self):
        Person.__init__(self, name = 'Gio')
        self.blood_of_the_tribe = self.blood_of_the_tribe + 0.25


        
class Jon(person):
    def __init__(self):
        Person.__init__(self, name = 'Jon')
        self.blood_of_the_tribe = self.blood_of_the_tribe + 1.00


        
class Nick(person):
    def __init__(self):
        Person.__init__(self, name = 'Nick')
        self.blood_of_the_tribe = self.blood_of_the_tribe


        
class Rajan(person):
    def __init__(self):
        Person.__init__(self, name = 'Rajan')
        self.blood_of_the_tribe = self.blood_of_the_tribe

        
