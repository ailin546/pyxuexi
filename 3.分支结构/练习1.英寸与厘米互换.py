"""
英寸与厘米互换   1英寸= 2.54厘米

Version： 0.1
Author: Ailin
"""

value = float(input("请输入长度："))
unit = input("请输入单位:")
if 'cm' in unit or '厘米' in unit:
    print("%.2f %s 转换成英寸为 %.2f 英寸" % (value,unit,value/2.54))
elif 'in' in unit or '英寸' in unit:
    print("%.2f %s 转换成厘米为 %.2f 厘米" % (value, unit,value*2.54))
else:
    print("您的输入有误！")