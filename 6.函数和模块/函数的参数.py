from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
"""
def add(a=0,b=0,c=1):
    return a+b+c 
"""
def add(*a):
    total = 0
    for i in a:
        total += i 
    return total
print(roll_dice(5))
print(roll_dice() )
print(add(1,2,3))
print(add())
