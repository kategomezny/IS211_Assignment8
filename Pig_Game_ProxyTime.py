#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pig Game against the computer"""

import argparse
import random
import time

parser = argparse.ArgumentParser(description="Num of players")
parser.add_argument('player1',type=str,help='Player 1')
parser.add_argument('player2',type=str,help='Player 2')
parser.add_argument('timed',type=str,help='Enter time (t) for a timed game')
args = parser.parse_args()


class Player():
    """Base class which stores player names"""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.type = 'h'
        
        print 'Welcome to the Pig Game, {}.'.format(self.name)


class ComputerPlayer(Player):
    """Inherited class from the Player class"""
    def __init__(self, name):
        Player.__init__(self, name)
        self.score = 0
        self.type = 'c'
        
        print ('Welcome Computer to the Pig Game')
        
    def computer_hold_or_roll(self,turn_score):
        limit = 100-self.score
        if turn_score > min(25,limit):
            return 'h'
        else:
            return 'r'        
        

class PlayerFactory():
    """Instantiate the correct Player class"""
    def Type_of_Player(self, Type_of_Player, name='Jacob'):
        if Type_of_Player == 'h':
            return Player(name)
        elif Type_of_Player == 'c':
            return ComputerPlayer(name)
        
class Game():
    def Pig_Game(self):
        local_Proxy = TimedGameProxy(Game)
        """Set up the rules of the game and number of players"""
        NewPlayer = PlayerFactory()    
        if args.player1 == 'h':
            player_name=raw_input("Please enter the name of player 1:")
            game_player1=NewPlayer.Type_of_Player('h',player_name)
        else:
            game_player1=NewPlayer.Type_of_Player('c','Computer1')
        if args.player2 == 'h':
            player_name=raw_input("Please enter the name of player 2:")
            game_player2=NewPlayer.Type_of_Player('h',player_name)
        else:
            game_player2=NewPlayer.Type_of_Player('c','Computer2')

            
        game="Start_game"
        previous_roll_die=0 
        Current_Player=game_player1
        while game != "Finish":
            x=0
            while x <  2:
                change_player = True
                if Current_Player==game_player1:
                   Current_Player=game_player2
                else:
                    Current_Player=game_player1
                
                while change_player == True:
                    local_Proxy.time_keeper(game_player1,game_player2)
                    if Current_Player.type == 'h':                    
                        roll_or_hold=raw_input(Current_Player.name + " Do you want to roll (r) the die or hold (h)?:")
                    else:
                        roll_or_hold=Current_Player.computer_hold_or_roll(previous_roll_die)
                        print (Current_Player.name + " Do you want to roll (r) the die or hold (h)?:" + roll_or_hold )
                    
                    if  roll_or_hold == "r":
                        roll_die = random.randint(1,6)
                        previous_roll_die=roll_die
                        if roll_die ==1:
                            print "    Roll = " + str(roll_die) + " | Sorry is next player's turn"
                            change_player = False
                        else: 
                            Current_Player.score = Current_Player.score + roll_die
                            if Current_Player.score >= 100:
                                print "    You are the winner with a total score of " + str(Current_Player.score)
                                game="Finish"
                                change_player = False
                                x=2
                            else:
                                print "    Roll = " + str(roll_die) + " Your Total score is= " + str(Current_Player.score)
                    elif roll_or_hold == "h":
                        change_player = False
                        print "Next player's turn"
                    elif roll_or_hold == "f":
                        change_player = False
                        x=2
                        game="Finish"
                        print "   bye bye"
                                
                    else:
                        change_player = False
                        print "    You lost your turn.  Next time please enter a correct option: r or h"
    
                x=x+1  


            
class TimedGameProxy(Game):
    """Keeps track of the time."""
    def __init__(self,start_time):
        """Constructor of the TimedGameProxy class."""
        self.start_time = time.time()


    def time_keeper(self,tk_player1,tk_player2):
        """the game starts, and should check that no more than 
        one minute has gone by since then at every step."""  
        if time.time() - self.start_time >= 60:
            if tk_player1.score > tk_player2.score:
                print ('Time is over! {} '
                       'won with a score '
                       'of {}.').format(tk_player1.name,
                                        tk_player1.score)
            else:
                print ('Time is over! {} '
                       'won with a score '
                       'of {}.').format(tk_player2.name,
                                        tk_player2.score)
                raise SystemExit
        else:
            time_left = time.time() - self.start_time
            print ('{} seconds have elapsed. Keep playing!').format(time_left)

   
def main():
     Proxy = TimedGameProxy(time.time)
     Proxy.Pig_Game()

        
if __name__== "__main__":
      main()
        
        
      
    

