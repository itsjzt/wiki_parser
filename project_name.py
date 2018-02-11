import random
import json

data = json.load(open('chip.json'))
chip_names = data["names"]
num = int(random.random() * len(chip_names))

# print(chip_names)
print(chip_names[num])
