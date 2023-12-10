#A Game of Cubes! No more than 12 red, 13 green, and 14 blue cubes can exist in a game set.

import re

file = open("./Data/cubes.txt", "r")

games = file.read().splitlines()

red_limit = 12
green_limit = 13
blue_limit = 14

id_sum = 0

for game_id, game_string in enumerate(games, 1):
    highest_red = 0
    highest_green = 0
    highest_blue = 0

    rounds = game_string.split(';')
    for round_data in rounds:
        counts = re.findall(r'(\d+)\s+(\w+)', round_data)
        for count, color in counts:
            count = int(count)
            if color == 'red' and count > highest_red:
                highest_red = count
            elif color == 'green' and count > highest_green:
                highest_green = count
            elif color == 'blue' and count > highest_blue:
                highest_blue = count
    if highest_red <= red_limit and highest_green <= green_limit and highest_blue <= blue_limit:
        id_sum += game_id

print(id_sum)

#Round 2, I HAVE THE POWERRRR!!!

file = open("./Data/cubes.txt", "r")

games = file.read().splitlines()

red_limit = 12
green_limit = 13
blue_limit = 14

powerrr = 0

for game_id, game_string in enumerate(games, 1):
    highest_red = 0
    highest_green = 0
    highest_blue = 0

    rounds = game_string.split(';')
    for round_data in rounds:
        counts = re.findall(r'(\d+)\s+(\w+)', round_data)
        for count, color in counts:
            count = int(count)
            if color == 'red' and count > highest_red:
                highest_red = count
            elif color == 'green' and count > highest_green:
                highest_green = count
            elif color == 'blue' and count > highest_blue:
                highest_blue = count
    round_powerrr = max(highest_blue, 1) * max(highest_green, 1) * max(highest_red, 1)
    powerrr += round_powerrr

print(powerrr)
