import re

def mapping(samples_file):

    with open(samples_file, "r") as file:
        samples = file.read()

    sections = samples.split('\n\n')

    seeds = [int(num) for num in re.findall(r'\d+', sections[0])]

    strmaps = []
    maps = []
    locations = []

    for section in sections[1:]:
        lines = section.split('\n')
        strmaps.append(lines[1:])

    for strmap in strmaps:
        triplets = []
        for string in strmap:
            numbers = list(map(int, string.split()))
            triplets.append(numbers)
        maps.append(triplets)

    for seed in seeds:
        for m in maps:
            for r in m:
                if seed in range(r[1],(r[1] + r[2])):
                    seed += (r[0]-r[1])
                    break
        locations.append(seed)

    print (min(locations))

mapping("./Data/samples.txt")
