#Island Island lottery

import re

file = open("./Data/scratchcards.txt", "r")
lines = file.readlines()

winning_numbers = []
picked_numbers = []
scratch_score = 0

for scratch_id, line in enumerate(lines, 1):

    #Gather the winning numbers for a card
    
    matches = re.search( r':\s*([\d\s]+)\s*\|' , line)
    if matches:
        winning_numbers = matches.group(1).split()

    #Gather the selected numbers for a card

    matches = re.search( r'\|\s*([\d\s]+)\s*' , line)
    if matches:
        picked_numbers = matches.group(1).split()

    matched_numbers = set(winning_numbers).intersection(picked_numbers)

    combo = 0
    if len(matched_numbers) > 0:
        for number in matched_numbers:
            if combo == 0:
                combo = 1
            else:
                combo = combo * 2 
        scratch_score += combo

print(scratch_score)