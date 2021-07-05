"""
将华氏温度转化为摄氏温度

Version： 0.1
Author：Ailin

"""

f = float(input("请输入华氏温度："))
c = (f - 32)/ 1.8
#print("%.1f华氏度 =%.2f摄氏度 " %(f,c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')