"""
正整数的反转

Version: 0.1
Author: Ailin
"""
"""
num = int(input("请输入一个正整数："))
recover_num = 0
i = 0
while True:
    i += 1
    if num <= 10 ** i:
        i = i-1
        break;
if i >=2 :
    for j in range(i,-1,-1):
        recover_num += (num//10**j)%10 * 10**(i-j)
    print("%d翻转后为%d" % (num,recover_num))
else:
    print("%d翻转后仍为%d" % (num,num))
"""

num = int(input("请输入正整数:"))
recover_num = 0
while num>0:
    recover_num = recover_num *10 + num % 10
    num //= 10
print("翻转后为%d"%(num,recover_num))