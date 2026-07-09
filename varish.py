import random
import string

name = ""

for i in range(8):
    name += random.choice(string.ascii_lowercase)

print(name + ".txt")