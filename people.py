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
    person.__init__()
    pass

class caleb(person):
    person.__init__()
    pass

class gio(person):
    person.__init__()
    pass

class jon(person):
    person.__init__()
    pass

class nick(person):
    person.__init__()
    pass

class rajan(person):
    person.__init__()
    pass
