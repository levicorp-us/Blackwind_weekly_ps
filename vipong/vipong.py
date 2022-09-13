import math
import random

def throw(l: float, d: float) -> bool:
    startpoint = random.uniform(0, d)
    rand_angle = random.uniform(-90, 90)
    return (startpoint + l * math.cos(math.radians(rand_angle))) >= d

def cal_pi(l: float, d: float, n: int) -> float:
    num_success = 0
    for i in range(n):
        if throw(l,d) == True:
            num_success += 1
    prob = num_success/n
    return (2 * l) / (d * prob)

print(cal_pi(10, 20, 1000000))