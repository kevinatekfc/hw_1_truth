# samplit: random 1 percent sampler - targer version
import sys
import random

filename = sys.argv[1]
file = open(filename)

for line in file:
    number = random.random()
    if number < 0.01:
        print(line, end="")

file.close()
