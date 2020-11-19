"""
Character definitions
"""
from random import randint
from collections import OrderedDict

class cognitiveShadow:
    """
    !!!
    """
    def __init__(self, name, insight):
        self.stats['insight'] = insight + 20
        self.stats['name'] = f"{name}'s Shade'"
        self.stats['bound'] = None
    
    def corporeate(self):
        self.bound = True

    def banish(self):
        self.bound = False

class Person:
    """
    A human bean.
    """

    def __init__(self, name, insight = 0, health = 100, blood_of_the_tribe = 0):
        self.inventory = {}
        self.stats = OrderedDict()
        self.stats['name'] = name
        self.stats['alive'] = None
        self.stats['insight'] = 0
        self.stats['health'] = 100
        self.stats['blood_of_the_tribe'] = 0

    def spawn(self):
        self.stats['alive'] = True
        print(f"A wild {self.stats['name']} has spawned.\n")

    def die(self):

        if self.stats['alive'] == True:

            death_msgs = [
                f"{self.stats['name']} couldn't hang. RIP.",
                f"{self.stats['name']} ded."
            ]

            print(death_msgs[randint(0, len(death_msgs) - 1)])

            if self.stats['insight'] > 50:
                globals()[f"shade_{self.stats['name']}"] = cognitiveShadow(self.stats['name'], self.stats['insight'])

        elif self.stats['alive'] == False:
            print("The dead cannot die.")

class Jeremy:
    """
    Just a Regular Guy!
    ----
    An Easter Egg while in Main Sequence. 
    Critical in Cognitive Shadow sequence.
    Allows asynchronous calls to SpankSquad Slack Workspace that waits for input from Slack users.
    """
    
    def __init__(self):
        pass

    def sendSlack(self):
        pass

    def readSlack(self, channel):
        pass