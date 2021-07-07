"""
斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。

Version: 0.1
Author: Ailin
"""
"""
num = int(input("您想取前多少位数值？"))
x = 1
y = 1
if num <= 0:
    print("您的输入有误！")
elif num == 1:
    print("斐波那契数列前%d个数值为" % num ,1)
elif num == 2:
    print("斐波那契数列前%d个数值为" % num ,1,1)
else:
    for i in range(num):
        print(x,end="\t")
        x,y = x+y,x
"""

x = 0
y = 1
for _ in range(20):
    x,y = y,x+y
    print(x,end=" ")