# maze-adventure
Python text-based cmd adventure game


The implementation of the game consists of several modules. These are:
- _goblin.py_ and _monster.py_, where the blueprints for NPC objects are created
- _maze_gen_recursive.py_, where the blueprint for a maze is created
- _rpsGame.py_ which contains the code for interaction with Gamer NPCs
- _hero.py_, in which the blueprint for a Hero object is created and the main actions the user can take are defined
- _playgame.py_ in which all modules are imported and the main behavior of the game is defined


In order to play the game, the user has to open the Command Line Terminal, navigate to the folder in which all files are located with the cd command and then type in “python playgame.py”. This will execute the main module and start the program.

### Rules

The rules of the game are fairly simple. The player has to navigate through a maze filled with friendly goblins and 
hostile monsters. He or she starts with 1000 coins and 100 health points. Having in mind each move costs a health 
point, he or she has to **meet** _all_ monsters while simultaneously accumulating as many coins as possible.

Wealth Goblins can give coins based on a random probability, Thief Monsters can take them away.
Health Goblins and Fighter Monsters operate on the same basis but with health points instead of coins. 

Encounters with Gamer Goblins and Gamer Monsters are decided with a game of Rock Paper Scissors. 

When the program is started, the ‘simulation’ begins, and all NPCs are deployed onto the “virtual arena” on a completely random basis.

A welcoming message explaining the rules appears and allows the user to choose a difficulty mode. This changes the probability that the user will receive aid when meeting a goblin or that he or she will lose resources when fighting a monster. The maze is generated and thus the trial can begin.

The Hero character is represented by the H symbol. The monsters are indicated by M and 
accordingly, the goblins are G. The spikes show where the user CAN NOT go and if the player chooses to move 
on such a tile, the Hero will simply refuse to move.

Pressing Z will allow the user to see the controls and available options, such as saving, loading, showing the map, etc.

If the user moves to the closest monster, they will discover that their Hero is equipped with a **radar** and will detect 
any NPCs in the area. In addition, it will inform them of the quantity of resources the NPC can give/steal and what the odds are of this happening.

Once all monsters are encountered and all medals are collected, the game asks for the name of the winner and then shows the Top 10 players on each difficulty mode, ending the execution of the program.
Players are ranked based on the number of coins in their posession.
