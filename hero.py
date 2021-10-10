#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import sys
import random
import rpsGame
import pickle

class Hero:
    """hero class"""
    def __init__(self, initialX, initialY):
        """constructor"""
        self._coordX = initialX # vertical coordinate of the hero in the maze
        self._coordY = initialY # horizontal coordinate of the hero in the maze
        self._health = 100 # health points
        self._coins = 1000  # gold coins the hero has
        self._medals = 0 # 5 needed to win the game
        self._difficulty = 0 # will change the chances of successful encounters if changed
        self._name = "" # used for ranking

    def actions(self, environment, goblinsInMaze, monstersInMaze, ch2):
        """select difficulty, see map, see help, move in the maze"""
        
        if ch2 == b'1':
            self._difficulty = 1
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            print("\nWe will go easy on you! \n\nGood luck!\n")
            return True
        elif ch2 == b'2':
            self._difficulty = 2
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            self.attr_changer(goblinsInMaze, monstersInMaze, 10) # slightly changes the odds of success
            print("\nWe will provide some challenge! Changing NPC attributes accordingly...\n\nGood luck!\n")
            return True
        elif ch2 == b'3':
            self._difficulty = 3
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            self.attr_changer(goblinsInMaze, monstersInMaze, 30) # notably changes the odds of success
            print("\nWe will test you to your extremes! Changing NPC attributes accordingly...\n\nGood luck!\n")
            return True
        elif ch2 == b'4':
            self._difficulty = 4
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            self.attr_changer(goblinsInMaze, monstersInMaze, 50) # significantly changes the odds of success
            print("\nWe will give you hell! Changing NPC attributes accordingly...\n\nGood luck!\n")
            return True
        elif ch2 == b'Q':
            environment.print_environment # print map without moving
            print("\nThis is the current map.\nH - Hero || G - Goblin Friend || M - Monster Enemy\n")
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            return True
        elif ch2 == b'Z':
            print("\nUse the arrows to move. Press 'Q' to see the map. Save your game with 'S' and come back to it later with 'L'. \n") # help
            self._health += 1 # compensates for health taken away for each action in main module since this is not a hero movement
            return False 
        elif ch2 == b'H' or ch2 == "A":
            # the up arrow key was pressed
            print ("\nYou pressed 'up'\n")
            
            val = environment.get_coord(self._coordX - 1, self._coordY) # checks next tile
            val2 = environment.get_coord(self._coordX - 2, self._coordY) # checks the tile after the next tile

            if val == 3 and val2 == 0: # if next tile is a goblin and the tile after is free
                self._coordX = self._coordX - 2 # set hero coordinates to tile after
                environment.set_coord(self._coordX, self._coordY, 2) # move hero icon to new coordinates
                environment.set_coord(self._coordX + 2, self._coordY, 0) # clear the icon from old coordinates
                environment.set_coord(self._coordX + 1, self._coordY, 0) # clear the goblin icon (goblins disappear after interaction)
                for goblin in goblinsInMaze: # check each goblin to find out which one was the one the hero just passed
                    if self._coordX + 1 == goblin._coordX and self._coordY == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType()) # interact with goblin
                return True
            elif val == 3 and val2 != 0: # if next tile is a goblin and the tile after is not free
                environment.set_coord(self._coordX - 1, self._coordY, 0) # clear the goblin icon (goblins disappear after interaction)
                for goblin in goblinsInMaze: # check each goblin to find out which one was the one the hero just passed
                    if self._coordX - 1 == goblin._coordX and self._coordY == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType()) # interact with goblin
                return True
            elif val == 4 and val2 == 0: # if next tile is a monster and the tile after is free
                self._coordX = self._coordX - 2 # set hero coordinates to tile after
                environment.set_coord(self._coordX, self._coordY, 2) # move hero icon to new coordinates
                environment.set_coord(self._coordX + 2, self._coordY, 0) # clear the icon from old coordinates without clearing the monster icon (monsters do not disappear after interaction)
                for monster in monstersInMaze: # check each monster to find out which one was the one the hero just passed
                    if self._coordX + 1 == monster._coordX and self._coordY == monster._coordY:
                        self.fight_monsters(monster, monster.strType()) # interact with monster
                return True
            elif val == 4 and val2 != 0: # if next tile is a monster and the tile after is not free
                for monster in monstersInMaze: # check each monster to find out which one was the one the hero just passed
                    if self._coordX - 1 == monster._coordX and self._coordY == monster._coordY:
                        self.fight_monsters(monster, monster.strType()) # interact with monster
                return True
            elif not val: # if next tile is free
                self._coordX = self._coordX - 1 # set hero coordinates to next tile
                environment.set_coord(self._coordX, self._coordY, 2) # move hero icon to new coordinates
                environment.set_coord(self._coordX + 1, self._coordY, 0) # clear the icon from old coordinates
                return True
            else:
                return False


        elif ch2 == b'P' or ch2 == "B":
            # the down arrow key was pressed ----- everything after is on the same principle as the code for up arrow key
            print ("\nYou pressed 'down'\n")
            
            val = environment.get_coord(self._coordX + 1, self._coordY)
            val2 = environment.get_coord(self._coordX + 2, self._coordY)

            if val == 3 and val2 == 0:
                self._coordX = self._coordX + 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX - 2, self._coordY, 0)
                environment.set_coord(self._coordX - 1, self._coordY, 0)
                for goblin in goblinsInMaze:
                    if self._coordX - 1 == goblin._coordX and self._coordY == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 3 and  val2 != 0:
                environment.set_coord(self._coordX + 1, self._coordY, 0)
                for goblin in goblinsInMaze:
                    if self._coordX + 1 == goblin._coordX and self._coordY == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 4 and val2 == 0:
                self._coordX = self._coordX + 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX - 2, self._coordY, 0)
                for monster in monstersInMaze:
                    if self._coordX - 1 == monster._coordX and self._coordY == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif val == 4 and val2 != 0:
                for monster in monstersInMaze:
                    if self._coordX + 1 == monster._coordX and self._coordY == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif not val:
                self._coordX = self._coordX + 1
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX - 1, self._coordY, 0)
                return True
            else:
                return False


        elif ch2 == b'K' or ch2 == "D":
            # the left arrow key was pressed ----- everything after is on the same principle as the code for up arrow key
            print ("\nYou pressed 'left'\n")
            
            val = environment.get_coord(self._coordX, self._coordY - 1)
            val2 = environment.get_coord(self._coordX, self._coordY - 2)
            
            if val == 3 and val2 == 0:
                self._coordY = self._coordY - 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY + 2, 0)
                environment.set_coord(self._coordX, self._coordY + 1, 0)
                for goblin in goblinsInMaze:
                    if self._coordX == goblin._coordX and self._coordY + 1 == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 3 and val2 != 0:
                environment.set_coord(self._coordX, self._coordY - 1, 0)
                for goblin in goblinsInMaze:
                    if self._coordX == goblin._coordX and self._coordY - 1 == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 4 and val2 == 0:
                self._coordY = self._coordY - 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY + 2, 0)
                for monster in monstersInMaze:
                    if self._coordX == monster._coordX and self._coordY + 1 == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif val == 4 and val2 != 0:
                for monster in monstersInMaze:
                    if self._coordX == monster._coordX and self._coordY - 1 == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif not val:
                self._coordY = self._coordY - 1
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY + 1, 0)
                # print (self._coordX, self._coordY)
                return True
            else:
                return False

        elif ch2 == b'M' or ch2 == "C":
            # the right arrow key was pressed ----- everything after is on the same principle as the code for up arrow key
            print ("\nYou pressed 'right'\n")
            
            val = environment.get_coord(self._coordX, self._coordY + 1)
            val2 = environment.get_coord(self._coordX, self._coordY + 2)
        
            if val == 3 and val2 == 0:
                self._coordY = self._coordY + 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY - 2, 0)
                environment.set_coord(self._coordX, self._coordY - 1, 0)
                for goblin in goblinsInMaze:
                    if self._coordX == goblin._coordX and self._coordY - 1 == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 3 and val2 != 0:
                environment.set_coord(self._coordX, self._coordY + 1, 0)
                for goblin in goblinsInMaze:
                    if self._coordX == goblin._coordX and self._coordY + 1 == goblin._coordY:
                        self.meet_goblins(goblin, goblin.strType())
                return True
            elif val == 4 and val2 == 0:
                self._coordY = self._coordY + 2
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY - 2, 0)
                for monster in monstersInMaze:
                    if self._coordX == monster._coordX and self._coordY - 1 == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif val == 4 and val2 != 0:
                for monster in monstersInMaze:
                    if self._coordX == monster._coordX and self._coordY + 1 == monster._coordY:
                        self.fight_monsters(monster, monster.strType())
                return True
            elif not val:
                self._coordY = self._coordY + 1
                environment.set_coord(self._coordX, self._coordY, 2)
                environment.set_coord(self._coordX, self._coordY - 1, 0)
                return True
            else:
                return False

        return False

    def set_coord(self, x, y):
        """define coordinates of the hero"""
        self._coordX = x
        self._coordY = y

    def get_coord(self):
        """obtain the location of the hero"""
        return self._coordX, self._coordY

    def attr_changer(self, goblinsInMaze, monstersInMaze, value):
        """change the odds of success depending on the difficulty set by the user"""
        for goblin in goblinsInMaze:
            goblin._probability -= value # reduces the chance of getting an award from goblins
            if goblin._probability <= 0:
                goblin._probability = 0
        for monster in monstersInMaze:
            monster._probability += value # increases the chance of getting punished by monsters
            if monster._probability >= 100:
                monster._probability = 100

    def pre_meet(self, friend, friendType):
        """pre-information for possible results when in the proximity of a goblin"""
        print("\nYou Are Near " + str(friend) + "")
        if friendType == "WealthGoblin":
            print("You may receive " + str(friend._coins) + \
                " coins. The chance of that happening is " + str(friend._probability) + "%")
        elif friendType == "HealthGoblin":
            print("You may receive " + str(friend._health) + \
                " health points. The chance of that happening is " + str(friend._probability) + "%")
        elif friendType == "GamerGoblin":
            print("If you beat him in his game, you can win " + str(friend._coins) + \
                " coins and " + str(friend._health) + " health points. Will you try your luck? ")

    def pre_fight(self, enemy, enemyType):
        """pre-information for possible results when in the proximity of a monster"""
        print("You Are Near " + str(enemy) + "")
        if enemyType == "ThiefMonster":
            print("You might lose " + str(enemy._coins) + \
                " coins. The probability of this is " + str(enemy._probability) + "%")
        elif enemyType == "FighterMonster":
            print("You might lose " + str(enemy._health) + \
                " health points. The chance of that happening is " + str(enemy._probability) + "%")
        elif enemyType == "GamerMonster":
            print("If you lose in his game, he can take " + str(enemy._coins) + \
                " coins and " + str(enemy._health) + " health points. Will you try your luck? ")

    def radar(self, environment, fgroup, engroup):
        """scan the area for friend or foes so that pre-information can be displayed"""
        for fmember in fgroup:
            if environment.get_coord(self._coordX + 1, self._coordY) == 3 and fmember._coordX == self._coordX + 1 and fmember._coordY == self._coordY: # if there is a goblin object south of the hero and his icon hasn't been deleted yet
                self.pre_meet(fmember, fmember.strType()) # display pre-information 
            elif environment.get_coord(self._coordX, self._coordY + 1) == 3 and  fmember._coordX == self._coordX and fmember._coordY == self._coordY + 1: # analog for east
                self.pre_meet(fmember, fmember.strType())
            elif environment.get_coord(self._coordX - 1, self._coordY) == 3 and fmember._coordX == self._coordX - 1 and fmember._coordY == self._coordY: # analog for north
                self.pre_meet(fmember, fmember.strType())
            elif environment.get_coord(self._coordX, self._coordY - 1) == 3 and fmember._coordX == self._coordX and fmember._coordY == self._coordY - 1: # analog for south
                self.pre_meet(fmember, fmember.strType())

        for enmember in engroup: # analog for monsters
            if enmember._coordX == self._coordX + 1 and enmember._coordY == self._coordY:
                self.pre_fight(enmember, enmember.strType())
            elif enmember._coordX == self._coordX and enmember._coordY == self._coordY + 1:
                self.pre_fight(enmember, enmember.strType())
            elif enmember._coordX == self._coordX - 1 and enmember._coordY == self._coordY:
                self.pre_fight(enmember, enmember.strType())
            elif enmember._coordX == self._coordX and enmember._coordY == self._coordY - 1:
                self.pre_fight(enmember, enmember.strType())


    def meet_goblins(self, friend, friendType):
        """interact with goblins/after-meeting information"""
        print("You Just Talked With " + str(friend) + "")
        if friendType == "WealthGoblin":
            if random.randint(0, 101) < friend._probability: # use the odds to determine the outcome
                print("You received no coins...")
            else:
                self._coins += friend._coins
                print("You won " + str(friend._coins) + " coins!")
        elif friendType == "HealthGoblin":
            if random.randint(0, 101) < friend._probability: # use the odds to determine the outcome
                print("You received no health points...")
            else:
                self._health += friend._health
                print("You won " + str(friend._health) + " health points!")
        elif friendType == "GamerGoblin":
                if rpsGame.playRTS() == 2: # use the rock paper scissors module to determine the outcome
                    print("You lost the game and got nothing...")
                else:
                    self._health += friend._health
                    self._coins += friend._coins
                    print("You won " + str(friend._health) + " health points and " + str(friend._coins) + " coins! ")
        print("\nYou now have " + str(self._health - 1) + " health and " + str(self._coins) + " coins. ") # subtraction of 1 from health compensates for life taken from movement in main module

    def fight_monsters(self, enemy, enemyType):
        """fight with monsters/after-fight information"""  # analog to meet_goblins
        print("You Just Fought " + str(enemy) + "")
        self._medals += enemy._medals
        enemy._medals = 0
        if enemyType == "ThiefMonster":
            if random.randint(0, 101) < enemy._probability:
                self._coins -= enemy._coins
                if self._coins < 0:
                    self._coins == 0
                print("You just lost " + str(enemy._coins) + " coins...")
            else:
                print("Your coin purse is safe for now.")
        elif enemyType == "FighterMonster":
            if random.randint(0, 101) < enemy._probability:
                self._health -= enemy._health
                print("You lost " + str(enemy._health) + " health points...")
            else:
                print("You pass unharmed.")
        elif enemyType == "GamerMonster":
                if rpsGame.playRTS() == 2:
                    self._health -= enemy._health
                    self._coins -= enemy._coins
                    if self._coins < 0:
                        self._coins == 0
                    print("You lost " + str(enemy._health) + " health points and " + str(enemy._coins) + " coins... ")
                else:
                    print("You kicked his butt! ")
        print("\nYou now have " + str(self._health - 1) + " health and " + str(self._coins) + " coins. ")
    
    def win_state(self): 
        """check if hero has met all monsters"""
        numberMedals = self._medals
        if numberMedals == 5:
            print('\nYOU WON THE GAME! YOU COLLECTED A TOTAL OF ' + str(self._coins) + " COINS! \n")
            return True

    def fail_state(self):
        """check if hero was killed"""
        numberHP =  self._health
        if numberHP <= 0:
            print('\nYOU DIED! THE MONSTERS WILL SHARE THE ' + str(self._coins) + " COINS YOU HAD LEFT...\n")  
            return True   

    
