"""
输入三角形边长，计算三角形周长和面积
面积用海伦公式得：是s（s-a)(s-b)（s-c） **0.5
s = (a+b+c) /2
VERSION: 0.1
Author: Ailin

"""
a = float(input("请输入第一条边长："))
b = float(input("请输入第二条边长："))
c = float(input("请输入第三条边长："))
if a+b>c and a+c >b and b+c > a :
    s = (a + b+c)/2
    area = (s*(s-a )*(s-b )*(s-c ))**0.5
    print("三角形周长为%.2f" % (a+b+c))
    print("三角形面积为%.2f" % area )
else:
    print("无法构成三角形")