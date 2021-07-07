"""
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。

Version: 0.1
Author: Ailin
"""
import math 

for num in range(1,101):
#    factor = 0
    is_prime = True 
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0 :
#            factor += 1
            is_prime = False
    if is_prime :
        print(num,end=" ")