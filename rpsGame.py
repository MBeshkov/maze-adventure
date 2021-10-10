from getch1 import *
import sys
import random

def playRTS():
    """function for rock paper scissors duel with the gamer goblin and gamer monster"""
    rps_array =  ['rock', 'paper', 'scissors'] # possible choices
    comp_choice = ''
    user_choice = ''
    gameOver = False

    while not gameOver:
        print('You have been challenged to a duel! Enter R for "rock", P for "paper" or S for "scissors"!')
        comp_choice = random.choice(rps_array) # computer choice is random
        
        userInput = getch().upper() # user choice is manual and instantenous (no need for 'enter')
    
        if userInput == b'R':
            user_choice = rps_array[0]
        elif userInput == b'P':
            user_choice = rps_array[1]
        elif userInput == b'S':
            user_choice = rps_array[2]
        else:
            print("\nTrying tricks, are ye?\n")
            return 2 # game is a loss if any other button is pressed
            
        
        val1 = user_choice
        val2 = comp_choice
        i1 = rps_array.index(val1) 
        i2 = rps_array.index(val2) 
        d = (i1 - i2) % len(rps_array) # return 1 if player is winner, 2 for lose, 0 for tie

        if d == 2:
            print("\nNice try but he picked " + comp_choice + ". You lost... \n")
            gameOver = True
            return d
        elif d == 1:
            print("\nHe picked " + comp_choice + ". You won!\n")
            gameOver = True
            return d
        elif d == 0:
            print("\nTie, play again!\n")
            


