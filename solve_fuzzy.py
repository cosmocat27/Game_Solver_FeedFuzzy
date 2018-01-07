# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:06:44 2018

@author: cosmo
"""

from play_fuzzy import play_fuzzy
from math import sqrt
import sys


number_players = 2

def sim_play_fuzzy(p1_state, p2_state, on_move, die_colors, die_numbers, n):
    win_count_p = {-1: 0}
    move_count_p = {-1: 0}
    for i in range(1, number_players+1):
        win_count_p[i] = 0
        move_count_p[i] = 0
    for i in range(n):
        p_win, move_count = play_fuzzy(p1_state, p2_state, on_move, die_colors, die_numbers)
        print(p_win, move_count)
        win_count_p[p_win] += 1
        move_count_p[p_win] += move_count
    
    print("Total games: ", n)
    for i in range(1, number_players+1):
        print()
        print("Player {} wins: {} ({}%)".format(i, win_count_p[i], round(100*win_count_p[i]/n)))
        p_mod = (win_count_p[i]+2)/(n+4)
        sd = sqrt(p_mod*(1-p_mod)/(n+4))
        print("Uncertainty (95% confidence): +/-{}%".format(round(100*1.96*sd, 1)))
        print("Average number of moves: {}".format(round(move_count_p[i]/n, 1)))


if __name__ == '__main__':
    
    die_colors = ['O', 'Y', 'G', 'B', 'P', 'W']
    die_numbers = [1, 1, 1, 2, 2, 3]
    
    p1_state = {'O':3, 'Y':3, 'G':3, 'B':3, 'P':3}
    p2_state = {'O':3, 'Y':3, 'G':3, 'B':3, 'P':3}
    on_move = 1
    
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    
    sim_play_fuzzy(p1_state, p2_state, on_move, die_colors, die_numbers, n)

