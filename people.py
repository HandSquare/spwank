"""
Defines all our characters
"""

class person(object):

    def _init_(self):
        self.inventory = {}
        self.health = 100
        self.insight = 0
        self.alive = 0
    
    def spawn(self):
        self.alive = True

    def die(self):
        self.alive = False


class brian(person):
    pass

class caleb(person):
    pass

class gio(person):
    pass

class jon(person):
    pass

class rajan(person):
    pass