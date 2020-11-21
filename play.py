from entities import *
from pprint import pprint

# ==========================
# *** Character Creation ***
# ==========================

print("Welcome. Please enter your name: ")
init_name = input('> ')[0:33]

if len(init_name) > 8:
    print("That's a bit long... do you have a nick-name?")
    long_name = init_name
    char_name = input('> ')[0:8]

else:
    char_name = init_name

print(f"Ok, we'll call you {init_name}.")

# assigning variables like this lets us
# turn user input into variable names:
# this is important for the cognitive shadow sequence
player = globals()[char_name] = Person(char_name)

print("\n")
player.spawn()

print("Your stats: \n")
for stat, value in player.stats.items():
    print(f"\t{stat}: {value}")

print('\n')

print("Your inventory: ")
for stat, value in player.inventory.items():
    print(f"\t{stat}: {value}")

print("\n")

# =======================
# *** Jeremy Sequence ***
# =======================

jeremy = Jeremy(realm = 'Dark')
jeremy.sendSlack(
    message = f"Python test with [spwank] player: {player.stats['name']}!",
    channel = 'jeremys_in_a_sandbox'
)

print("\n")

# =====================
# *** Main Sequence ***
# =====================

# 60 insight available, need 50 to turn into a Cognitive Shadow when you die,
# which unlocks secret ending - otherwise, death means you lose

# =========================================
# *** SECRET: Cognitive Shadow Sequence ***
# =========================================

# some 4th wally shit where the user has to traverse the python env
# to find the blood of the tribe

# ====================
# *** End Sequence ***
# ====================

if player.stats['blood_of_the_tribe'] == 1.0:
    pass

elif player.stats['blood_of_the_tribe'] > 0.5:
    pass

elif player.stats['blood_of_the_tribe'] > 0.0:
    pass

else:
    print("Guess there was no blood of the tribe after all.")