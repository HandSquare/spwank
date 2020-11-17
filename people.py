"""
Defines all our characters
"""

class Person(object):

    def _init_(self, name):
        self.inventory = {}
        self.health = 100
        self.insight = 0
        self.alive = None
        self.name = name
    
    def spawn(self):
        self.alive = True

    def die(self):
        self.alive = False
        

class Brian(person):
    def __init__(self):
        Person.__init__(self, name = 'Brian')
        
class Caleb(person):
    def __init__(self):
        Person.__init__(self, name = 'Caleb')

        
class Gio(person):
    def __init__(self):
        Person.__init__(self, name = 'Gio')

        
class Jon(person):
    def __init__(self):
        Person.__init__(self, name = 'Jon')

        
class Nick(person):
    def __init__(self):
        Person.__init__(self, name = 'Nick')

        
class Rajan(person):
    def __init__(self):
        Person.__init__(self, name = 'Rajan')
        
