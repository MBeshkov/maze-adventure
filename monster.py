#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0
import random

class Monster:
    """blueprint for monsters"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        self._coordX = initialX # vertical
        self._coordY = initialY # horizontal
        self._health = 0 # health that monsters can take from hero
        self._coins = 0 # coins that monsters can take form hero
        self._probability = 0 # odds of interaction with hero being a success/failure
        self._monsterTypes = [ThiefMonster, FighterMonster, GamerMonster] # intital spawn of goblins of each type (as specified in requirements)
        self._generated_monsters = [] # container for all 5 spawns 

    def set_coord(self, x, y):
        """define coordinates of the monsters, used when deploying them"""
        self._coordX = x
        self._coordY = y

    def get_coord(self):
        """obtain the location of the monsters"""
        return self._coordX, self._coordY

    def generate_monsters(self):
        """randomly generates monsters"""
        self._generated_monsters = []
        for monsterType in self._monsterTypes:
            self._generated_monsters.append(monsterType()) # the obligatory three monsters of each type
        for x in range (0, 2):
            self._generated_monsters.append(random.choice(self._monsterTypes)()) # addition of two monsters of a random type
        return self._generated_monsters


class ThiefMonster(Monster):
    """thief monster blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._medals = 1 # reward for passing by a monster (5 medals win the game)
        self._coins = random.randint(50, 101) # random but in values that don't make the hero finish with too low of a score
        self._probability = random.randint(0, 101) # (changes when difficulty is changed)

    def __str__(self):
        """string representation of the monster"""
        return self.get_fullname()

    def strType(self):
        """string representation of the monster type (aka thief, fighter and gamer)"""
        return "ThiefMonster"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Thief Monster at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._coins) + ' coins and a success rate of ' + \
                str(self._probability) + '\n'
        return long_name.title()

class FighterMonster(Monster):
    """fighter monster blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._medals = 1 # reward for passing by a monster (5 medals win the game)
        self._health = random.randint(25, 51) # random but in values that don't make the hero die too quickly
        self._probability = random.randint(0, 101) # (changes when difficulty is changed)

    def __str__(self):
        """string representation of the monster"""
        return self.get_fullname()

    def strType(self):
        """string representation of the monster type (aka thief, fighter and gamer)"""
        return "FighterMonster"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Fighter Monster at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._health) + ' health and a success rate of ' + \
                str(self._probability) + '\n'
        return long_name.title()

class GamerMonster(Monster):
    """gamer monster blueprint"""
    def __init__(self, initialX = 0, initialY = 0):
        """constructor"""
        super().__init__(initialX, initialY) # inheritance
        self._medals = 1 # reward for passing by a monster (5 medals win the game)
        self._health = random.randint(25, 51) # random but in values that don't make the hero die too quickly
        self._coins = random.randint(50, 101) # random but in values that don't make the hero finish with too low of a score
        self._probability = 0 # (changes when difficulty is changed)

    def __str__(self):
        """string representation of the monster"""
        return self.get_fullname()

    def strType(self):
        """string representation of the monster type (aka thief, fighter and gamer)"""
        return "GamerMonster"

    def get_fullname(self):
        """returns a formatted string for initialisation report"""
        long_name = 'A Gamer Monster at coordinates ' + str(self._coordY) + ' and ' + \
            str(self._coordX) + ', with ' + str(self._health) + ' health and ' + str(self._coins) + ' coins\n' 
        return long_name.title()
    
 