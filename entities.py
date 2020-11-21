"""
Character definitions
(Some elements inspired by Brandon Sanderson's cosmere: https://coppermind.net/)
"""

from os import system
from random import randint
from collections import OrderedDict

github_raw_path = "https://raw.githubusercontent.com/"

class cognitiveShadow:
    """
    !!!
    """
    def __init__(self, name, insight):
        self.stats = OrderedDict()
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

    def __init__(self, realm):
        self.realm = realm
        self.jeremy_name = "Jeremy" if realm == "physical" else f"Jeremy in the {realm} Realm"
        self.source_path = github_raw_path + "nickells/jeremy-the-bot/master/sendCustomMessage.js"
        # TO DO: MAKE AND HOST RPG JEREMY ICON
        # TO DO: MAKE AND HOST JEREMY OF THE SHADOWS ICON


    def realmTraverse(self, dest, random = False):
        """
        Jeremy traverses the realms, himself beyond the limits of corporeation.

        Args:
            dest (str): a string that describes which realm jeremy should travel to. overriden by random if true. 
            random (bool): a boolean that describes whether jeremy should travel to a random realm or if he should follow 'dest'
        """
        random_realms = ['physical', 'cognitive', 'spiritual', 'transcendant', 'skeleton hell']
        # self.realm = travel_to_realm if random = False else  # replace with random from list of possible realms

    def sendSlack(self, channel, message):
        jeremy_name = self.jeremy_name
        # jeremy_path = self.source_path
        system(
            f"cd ~/repos/jeremy-the-bot &&\
              node sendCustomMessage.js c='{channel}' m='{message}' u='{jeremy_name}'"
        )

    def readSlack(self, channel, message):
        pass