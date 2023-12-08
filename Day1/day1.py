from enum import Enum
import re

file = open("./Data/calibration.txt","r")

lines = file.read().splitlines()

#Summary Calibration!

sum = 0
for line in lines:
    numline = re.sub(r"\D","",line)
    first_last = numline[0] + numline[-1]
    sum += int(first_last)

print("The Summary Calibration:", sum)

# The One True Summary Calibration!

file = open("./Data/calibration.txt","r")

lines = file.read().splitlines()

#Cheeky Innit? Why can't we have proper test results :(
class Digit(Enum):
    ONE = "o1e"
    TWO = "t2o"
    THREE = "t3e"
    FOUR = "f4r"
    FIVE = "f5e"
    SIX = "s6x"
    SEVEN = "s7n"
    EIGHT = "e8t"
    NINE = "n9e"

def replace_words(line):
    for word in Digit:
        line = line.replace(word.name.lower(), word.value)
    return line

modified_lines = [replace_words(line) for line in lines]

one_true_sum = 0
for line in modified_lines:
    numline = re.sub(r"\D","",line)
    first_last = numline[0] + numline[-1]
    one_true_sum += int(first_last)

print("The One True Summary Calibration:", one_true_sum)

