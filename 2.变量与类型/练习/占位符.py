"""
使用input()函数获取键盘输入
使用int()函数将输入的字符变成整数
使用print()函数输出带占位符的字符串
%d 整数占位符
%f 浮点数占位符
%% 百分号
%s 字符串

Version: 0.1
Author: Ailin

a = int(input("请输入任意数字a："))
b = int(input("请输入数字b="))
print("%d + %d = %d" % (a,b,a+b))
print("%d - %d = %d" % (a ,b, a-b))
print("%d * %d = %d" % (a, b, a*b ))
print("%d / %d = %f" % (a, b,a/b ))
print("%d %% %d = %d" % (a,b,a%b ))
print("%d ** %d = %d" % (a, b, a**b))
"""
print(int(float(input("请输入"))))