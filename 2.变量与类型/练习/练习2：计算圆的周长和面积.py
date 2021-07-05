"""
计算圆的周长和面积
周长= 2πr
面积= πr**2

Version: 0.1
Author: Ailin
"""
import math
r = float(input("请输入圆的半径："))
perimeter = math.pi *2 *r 
area = math.pi * r**2
print('圆的周长为：%.2f' % perimeter )
print("圆的面积为：%.2f " % area)