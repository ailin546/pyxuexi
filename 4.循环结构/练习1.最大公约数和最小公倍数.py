"""
计算两个数的最大公约数和最小公倍数

Version: 0.1
Author: Ailin
"""
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    x,y = y,x 
#如果x大，则互换数值
for z in range(x,0,-1):
    if x % z == 0 and y % z == 0:
        break;
print("最大公约数为%d" % z )
print("最小公倍数为%d" % (x*y/z))