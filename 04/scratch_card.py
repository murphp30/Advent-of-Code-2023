#!/usr/env python
import numpy as np

input_file = "input.txt"

total_points = []
card_tracker = {i:1 for i in range(1,200)}

with open(input_file) as f:
    for card in f:
        
        card_number, numbers = card.split(":")
        card_number = int(card_number.split()[1])
        split_numbers = numbers.split("|")
        winning_line = split_numbers[0].split()
        elf_line = split_numbers[1].split()
        matches = np.intersect1d(winning_line, elf_line)
        if len(matches) > 0:
            card_points = 1 * (2**(len(matches)-1))
        else:
            card_points = 0
        total_points.append(card_points)
        for i in range(card_number+1, card_number+1+len(matches)):
            card_tracker[i] = card_tracker[i] + card_tracker[card_number]
        

print("total points: {}".format(np.sum(total_points)))
print("total cards:", format(sum(card_tracker.values())))


