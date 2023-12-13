#Gondola gondola why have you broken down?
import re

file = open("./Data/schematic.txt", "r")
lines = file.readlines()

def process_grid(grid):
    number_and_surround = []
    
    #Given an index of row, start and end for a given number gather the surrounding characters as an array
    def get_surrounding_chars(row_idx, start_col_idx, end_col_idx):
        surrounding_chars = []
        for i in range(row_idx - 1, row_idx + 2):
            for j in range(start_col_idx - 1, end_col_idx + 2):
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                    if grid[i][j] == '\n':
                        surrounding_chars.append('') #Change new line to blank
                    else:
                        surrounding_chars.append(grid[i][j])
                else:
                    surrounding_chars.append('')  #If outside boundary use blank
        return surrounding_chars
    
    #Returns tuple of number value and array of surrounding characters by searching for numbers along with their 3 indices
    for row_idx, line in enumerate(grid):
        for match in re.finditer(r'\d+', line):
            start_col_idx, end_col_idx = match.span()
            number = match.group()
            surrounding = get_surrounding_chars(row_idx, start_col_idx, end_col_idx - 1)
            number_and_surround.append((number, surrounding))
    return number_and_surround

sum = 0
values = ['*','=','+','-','%','/','@','#','$','^','&','(',')','!']
result = process_grid(lines)

for number, surrounding_chars in result:
    for char in surrounding_chars:
        if any(char == val for val in values):
            sum += int(number)

print(sum)

# Grinding Gears Games presents...

import re

file = open("./Data/schematic.txt", "r")
lines = file.readlines()

def process_grid(grid):
    gear = {}
    
    def get_surrounding_chars(row_idx, start_col_idx, end_col_idx):
        surrounding_chars = []
        for i in range(row_idx - 1, row_idx + 2):
            for j in range(start_col_idx - 1, end_col_idx + 2):
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                    if grid[i][j] == '\n':
                        surrounding_chars.append('')  #Change new line to blank
                    else:
                        surrounding_chars.append(grid[i][j])
                        if grid[i][j] == '*':
                            #Record gear idx and touching number
                            gear[(i, j)] = gear.get((i, j), []) + [grid[row_idx][start_col_idx:end_col_idx + 1]]
                else:
                    surrounding_chars.append('')  #If outside boundary, use blank
        return surrounding_chars
    
    for row_idx, line in enumerate(grid):
        for match in re.finditer(r'\d+', line):
            start_col_idx, end_col_idx = match.span()
            get_surrounding_chars(row_idx, start_col_idx, end_col_idx - 1)

    return gear

big_gear_number = 0

gear_data = process_grid(lines)

for value in gear_data.values():
    temp = 0
    if len(value) == 2:
        temp = int(value[0])*int(value[1])
        big_gear_number += temp

print(big_gear_number)