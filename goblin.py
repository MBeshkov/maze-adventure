#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0
import random

class Goblin:
    """blueprint for goblins"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        self._coordX = initialX # vertical
        self._coordY = initialY # horizontal
        self._health = 0 # health that goblins can give to hero
        self._coins = 0 # coins that goblins can give to hero
        self._probability = 0 # odds of interaction with hero being a success/failure
        self._goblinTypes = [WealthGoblin, HealthGoblin, GamerGoblin] # intital spawn of goblins of each type (as specified in requirements)
        self._generated_goblins = [] # container for all 5 spawns 

    def set_coord(self, x, y):
        """define coordinates of the goblins, used when deploying them"""
        self._coordX = x
        self._coordY = y

    def get_coord(self):
        """obtain the location of the goblins"""
        return self._coordX, self._coordY
    
    def generate_goblins(self):
        """randomly generates goblins"""
        self._generated_goblins = []
        for goblinType in self._goblinTypes:
            self._generated_goblins.append(goblinType()) # the obligatory three goblins of each type
        for x in range (0, 2):
            self._generated_goblins.append(random.choice(self._goblinTypes)()) # addition of two goblins of a random type
        return self._generated_goblins

class WealthGoblin(Goblin):
    """wealth goblin blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._coins = random.randint(50, 101) # random but in values that don't make the hero accumulate too high of a score
        self._probability = random.randint(0, 101) # (changes when difficulty is changed in other modules)

    def __str__(self):
        """string representation of the goblin"""
        return self.get_fullname()

    def strType(self):
        """string representation of the goblin type (aka wealth, health and gamer)"""
        return "WealthGoblin"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Wealth Goblin at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._coins) + ' coins and a success rate of ' + \
                str(self._probability) + '\n'
        return long_name.title()

class HealthGoblin(Goblin):
    """health goblin blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._health = random.randint(25, 51) # random but in values that don't make the hero invinvcible 
        self._probability = random.randint(0, 101) # (changes when difficulty is changed in other modules)

    def __str__(self):
        """string representation of the goblin"""
        return self.get_fullname()

    def strType(self):
        """string representation of the goblin type (aka wealth, health and gamer)"""
        return "HealthGoblin"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Health Goblin at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._health) + ' health and a success rate of ' + \
                str(self._probability) + '\n'
        return long_name.title()

class GamerGoblin(Goblin):
    """gamer goblin blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._health = random.randint(25, 51) # random but in values that don't make the hero invinvcible
        self._coins = random.randint(50, 101) # random but in values that don't make the hero accumulate too high of a score
        self._probability = 0

    def __str__(self):
        """string representation of the goblin"""
        return self.get_fullname()

    def strType(self):
        """string representation of the goblin type (aka wealth, health and gamer)"""
        return "GamerGoblin"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Gamer Goblin at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._health) + ' health and ' + str(self._coins) + ' coins\n' 
        return long_name.title()

