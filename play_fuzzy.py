# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:49:01 2018

@author: cosmo
"""

from random import randrange


die_colors = ['O', 'Y', 'G', 'B', 'P', 'W']
die_numbers = [1, 1, 1, 2, 2, 3]

p1_state = {'O':3, 'Y':3, 'G':3, 'B':3, 'P':3}
p2_state = {'O':3, 'Y':3, 'G':3, 'B':3, 'P':3}
on_move = 1

class game_state:
    def __init__(self, p1_state, p2_state, on_move, die_colors, die_numbers):
        self.p1_state = p1_state
        self.p2_state = p2_state
        self.on_move = on_move
        self.die_colors = die_colors
        self.die_numbers = die_numbers
    
    def roll_dice(self):
        color = die_colors[randrange(5)] # ignore wilds for now
        number = die_numbers[randrange(6)]
        return color, number
    
    def remove_color(self, color, number, player = 0):
        if player == 0:
            player = self.on_move
        if player == 1:
            if self.p1_state[color] < number:
                self.on_move = 3 - self.on_move
                return False
            else:
                self.p1_state[color] -= number
                self.on_move = 3 - self.on_move
                return True
        else:
            if self.p2_state[color] < number:
                self.on_move = 3 - self.on_move
                return False
            else:
                self.p2_state[color] -= number
                self.on_move = 3 - self.on_move
                return True
        
    def change_state(self, player, new_state):
        if player == 1:
            self.p1_state = new_state
        else:
            self.p2_state = new_state
    
    def check_valid(self):
        for i in p1_state:
            if i < 0:
                return False
        for i in p2_state:
            if i < 0:
                return False
        return True
        
    def check_win(self):
        win1 = 1
        win2 = 1
        for color in p1_state:
            if p1_state[color] == 0:
                continue
            else:
                win1 = 0
                break
        for color in p2_state:
            if p2_state[color] == 0:
                continue
            else:
                win2 = 0
                break
        
        if win1 == 1 and win2 == 1:
            return -1
        elif win1 == 1:
            return 1
        elif win2 == 1:
            return 2
        else:
            return 0
            
    def get_state(self, player):
        if player == 1:
            return p1_state
        else:
            return p2_state
            

def main():
    game = game_state(p1_state, p2_state, on_move, die_colors, die_numbers)
    
    print("P1:", p1_state)
    print("P2:", p2_state)
    print("Player", on_move, "on move")
    
    move_count = 0
    while game.check_win() == 0:
        color, number = game.roll_dice()
        player = game.on_move
        print("P{}: {} {}".format(player, color, number))
        game.remove_color(color, number, player)
        print("P{}: {}".format(player, game.get_state(player)))
        if player == on_move:
            move_count += 1
        
    if game.check_win() == -1:
        print("There was an error!")
        return -1, move_count
    else:
        print("Player {} won in {} moves!".format(game.check_win(), move_count))
        return game.check_win(), move_count


if __name__ == '__main__':
    main()

