"""
输入M和N计算C(M,N)

Version: 0.1
Author: Ailin


m = int(input("M = "))
n = int(input("N = "))
while m<n:
    print("m不可以小于n，请重新输入：")
    m = int(input("M = "))
    n = int(input("N = "))
fm = 1 
for i in range(1,m+1):
    fm *= i
fn = 1
for i in range(1,n+1):
    fn *= i 
fmn = 1
for i in range(1,m-n+1):
    fmn *= i 
cmn = fm/(fn*fmn)
print("C(%d,%d) = %d" % (m,n,cmn))
"""

def fac(num):
    #求阶乘
    result = 1
    for i in range(1,num+1):
        result *= i
    return result 

m = int(input("m = "))
n = int(input("n = "))
while m < n :
    print("m不可以小于n，请重新输入：")
    m = int(input("M = "))
    n = int(input("N = "))
print("阶乘为:",fac(m)//fac(n) // fac(m-n ))