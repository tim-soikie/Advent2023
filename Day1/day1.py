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
