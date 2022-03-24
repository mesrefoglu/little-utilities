# inspired by Numberphile's video on YouTube: https://youtu.be/DmfxIhmGPP4

# the purpose of this code is to calculate the number of digits
#   of a reciprocal of a prime number until it starts repeating

import math

# needs to be prime input, or might get stuck
n = int(input())
m = 10 ** len(str(n))
o = m
c = 0

while True:
    m -= n * math.floor(m / n)
    m *= 10
    c += 1
    if m == o:
        print(c)
        break
