"""
输入年份 判断是否为闰年

Version: 0.1
Author: Ailin
"""
year = int(input("请输入整数年份"))
print(year % 4 == 0 and year % 100 != 0 ,(year % 4 == 0) & (year % 100 != 0) )
print(True | False)
is_leap = year % 4 == 0 & year % 100 != 0 
#| year % 400 == 0
print(is_leap)
if is_leap:
    print("%d是闰年" % year)
else:
    print("%d不是闰年" % year)