"""
打印九九乘法表

Version: 0.1
Author: Ailin
"""
for x in range(1,10):
    for y in range(1,10):
        print("%d*%d=%d" % (x, y ,x*y ),end = '\t')
        if y == 9:
            print("")