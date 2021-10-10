from getch1 import *
import sys
from hero import Hero
from goblin import Goblin
from monster import Monster
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
import random
import pickle

WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"
GOBLIN_CHAR = "G"
MONSTER_CHAR = "M"

X_DIMENSION = 17
Y_DIMENSION = 17

WIN_COUNTER = 0

class _Environment:
    """Environment includes Maze + Monsters + Goblins + Hero"""
    def __init__(self, maze):
        """constructor"""
        self._environment = deepcopy(maze)

    def set_coord(self, x, y, val):
        """set a tile to a goblin, monster or hero icon"""
        self._environment[x][y] = val

    def get_coord(self, x, y):
        """obtain the icon located at certain coordinates"""
        return self._environment[x][y]

    def print_environment(self):
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("0", SPACE_CHAR)  # replace the space character
            row_str = row_str.replace("1", WALL_CHAR)  # replace the wall character
            row_str = row_str.replace("2", HERO_CHAR)  # replace the hero character
            row_str = row_str.replace("3", GOBLIN_CHAR)  # replace the goblin character
            row_str = row_str.replace("4", MONSTER_CHAR)  # replace the monster character

            print("".join(row_str))
            
        print("")


class Game:

    def __init__(self):
        """constructor"""

        self.maze = make_maze_recursion(X_DIMENSION, Y_DIMENSION) # creates maze
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self.MyGoblin = Goblin() # new goblin object
        self.MyMonster = Monster() # new monster object
        self._goblinsInMaze = [] # container for future randomly generated goblins
        self._monstersInMaze = [] # container for future randomly generated monster
        self._easyRank = [] # container for winners on easy mode
        self._mediumRank = [] # container for winners on medium mode
        self._hardRank = [] # container for winners on hard mode
        self._vhardRank = [] # container for winners on very hard mode
        self.MyGoblin.generate_goblins() # generate random types of goblins (including the obligatory one instance of each type)
        self.MyMonster.generate_monsters() # generate random types of monsters (including the obligatory one instance of each type)

    def spawn_hero(self):
        """put hero on map"""
        while True:
            x = random.randint(2, X_DIMENSION - 2) # random coordinates
            y = random.randint(2, Y_DIMENSION - 2)
            if not self.MyEnvironment.get_coord(x,y): # checks for free tile
                self.MyEnvironment.set_coord(x,y,2) # prints hero icon on map
                self.myHero = Hero(x, y) # new hero object
                break

    def spawn_goblins(self):
        """put goblins on map"""
        i = 0
        while i <= 4: # five goblins
            x = random.randint(2, X_DIMENSION - 2) # random coordinates for each
            y = random.randint(2, Y_DIMENSION - 2)
            if not self.MyEnvironment.get_coord(x,y): # checks for free tiles
                self.MyEnvironment.set_coord(x,y,3) # prints goblin icon on map
                self.newGoblin = self.MyGoblin._generated_goblins[i] # new goblin object based on the randomly generated types
                self.newGoblin.set_coord(x, y) # set the coordinates of the new goblin
                self._goblinsInMaze.append(self.newGoblin) # add goblin to the container with goblin objects
                i += 1

    def spawn_monsters(self):
        """put monsters on map"""
        n = 0
        while n <= 4: # five monsters
            x = random.randint(2, X_DIMENSION - 2) # random coordinates for each
            y = random.randint(2, Y_DIMENSION - 2)
            if not self.MyEnvironment.get_coord(x,y): # checks for free tiles
                self.MyEnvironment.set_coord(x,y,4) # prints monster icon on map
                self.newMonster = self.MyMonster._generated_monsters[n] # new monster object based on the randomly generated types
                self.newMonster.set_coord(x, y) # set the coordinates of the new monster
                self._monstersInMaze.append(self.newMonster) # add monster to the container with monster objects
                n += 1
    
    def goblins_info(self):
        """initialisation report for goblins"""
        print("\nThe goblins just entered the maze!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for m in range (0, len(self._goblinsInMaze)):
            print(self._goblinsInMaze[m]) 
    
    def monsters_info(self):
        """initialisation report for monsters"""
        print("Oh no... the monsters spawned too!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for m in range (0, len(self._monstersInMaze)):
            print(self._monstersInMaze[m]) 

    def welcomingMsg(self):
        """introduction"""
        print("\nThe trial is about to start. Goblins are friendly, Monsters... not so much.")
        print("You are wounded. Each step in the maze drains your health points.")
        print("Meeting a Wealth Goblin can bring you goodies, a Health Goblin can revive you and if you beat a Gamer goblin at Rock Paper Scissors, you reaallly get spoiled.")
        print("Passing by the Monsters, however, can have the opposite effect - you can lose a lot! What you gain, though, is a medal for each monster you encounter.")
        print("Get all medals before your health drops to 0 and you win!")
        print("\nTo start, choose difficulty. Press '1' for easy, '2' for medium, '3' for hard and '4' for very hard.\n")

    def interface(self):
        """game status information"""
        print("Coins:", self.myHero._coins, "| Remaining health:", str(self.myHero._health), "| Medals:", self.myHero._medals,)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                Press 'Z' for help\n")

    def leagues(self):
        """ranking for each difficulty level"""
        with open("rank.pickle", "rb") as score_file: # open pickle file containing winners and load the hero objects in an array
            self._scores = []
            while True:
                try:
                    self._scores.append(pickle.load(score_file))
                except EOFError:
                    break
            score_file.close()
        
        for score in self._scores: # distribute objects in the lists with winners based on difficulty
            if score._difficulty == 1:
                self._easyRank.append(score)
            elif score._difficulty == 2:
                self._mediumRank.append(score)
            elif score._difficulty == 3:
                self._hardRank.append(score)
            elif score._difficulty == 4:
                self._vhardRank.append(score)

        # sort all winner lists based on coins collected druing their playthrough
        self._easyRank.sort(key=lambda x: x._coins, reverse=True)
        self._mediumRank.sort(key=lambda x: x._coins, reverse=True)
        self._hardRank.sort(key=lambda x: x._coins, reverse=True)
        self._vhardRank.sort(key=lambda x: x._coins, reverse=True)

        # print the top 10 players in each difficulty
        print("\nTop 10 heroes on Easy:\n")
        for rank in self._easyRank[0:10]:
            print('>>', rank._name, "--", rank._coins, "coins")
        print("\nTop 10 heroes on Medium:\n")
        for rank in self._mediumRank[0:10]:
            print('>>' , rank._name, "--", rank._coins, "coins")
        print("\nTop 10 heroes on Hard:\n")
        for rank in self._hardRank[0:10]:
            print('>>   ', rank._name, "--", rank._coins, "coins")
        print("\nTop 10 heroes on Very Hard:\n")
        for rank in self._vhardRank[0:10]:
            print('>>', rank._name, "--", rank._coins, "coins")


    def play(self):
        """game behaviour"""

        self.spawn_hero() # put hero on map
        self.spawn_goblins() # put goblins on map
        self.spawn_monsters() # put monsters on map
        self.goblins_info() # initialisation report for goblins
        self.monsters_info() # initialisation report for monsters
        self.welcomingMsg() # introduction to the game

        
        while True:

            ch2 = getch().upper() # continually take input from user

            if ch2 == b'S': # save game
                print("\nGame saved successfully!\n\n")
                entryS = {} # create a new dictionary
                entryS['environment'] = self.MyEnvironment
                entryS['goblinsInMaze'] = self._goblinsInMaze
                entryS['monstersInMaze'] = self._monstersInMaze
                entryS['hero'] = self.myHero
                with open('save.pickle', 'wb') as f: # open a pickle file
                    pickle.dump(entryS, f) # save the dictionary containing the environment, hero and all npc objects (overwrites existing data)
                    f.close()
            elif ch2 == b'L': # load game
                print("\nGame loaded successfully!\n\n") 
                entry = {} # create a new dictionary
                f = open('save.pickle', 'rb') # open the pickle file
                entry = pickle.load(f) # load all objects from the saved dictionary
                self.MyEnvironment = entry['environment']
                self._goblinsInMaze = entry['goblinsInMaze']
                self._monstersInMaze = entry['monstersInMaze']
                self.myHero = entry['hero']
                f.close()
                self.MyEnvironment.print_environment() # update map on screen
                self.interface() # game status information
                self.myHero.radar(self.MyEnvironment, self._goblinsInMaze, self._monstersInMaze) # detect npc objects in neighbouring tiles
            elif self.myHero.actions(self.MyEnvironment, self._goblinsInMaze, self._monstersInMaze, ch2): # behaviour when any other action is taken
                self.MyEnvironment.print_environment() # update map on screen
                self.myHero._health -= 1 # take one health point away
                self.interface() # game status information
                self.myHero.radar(self.MyEnvironment, self._goblinsInMaze, self._monstersInMaze) # detect npc objects in neighbouring tiles
                if self.myHero.win_state(): # if all monsters are met
                    self.myHero._name = input("What is your name, legendary warrior?\n") # request the name of the user
                    with open('rank.pickle', 'ab') as f: # open pickle file containing winners and save the hero object inside
                        pickle.dump(self.myHero, f)
                        f.close()
                    self.leagues()
                    print("\n\nThank you for playing, "  + str(self.myHero._name) + "!\n\n")
                    break
                if self.myHero.fail_state():
                    print("\n\nThank you for playing!\n\n")
                    break
            
            
                

if __name__ == "__main__":

    myGame = Game()
    myGame.play()
    