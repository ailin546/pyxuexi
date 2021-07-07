"""
猜数字游戏

Version: 0.1
Author: Ailin
"""
import random
answer = random.randint(1,100)
print(answer)
counter = 0
while True:
    number = int(float(input("请输入你猜的数字：")))
    counter += 1
    if number == answer :
        print("恭喜你猜对了，只用了%d次" % counter )
        break
    elif counter >= 6:
        if number == answer :
            print("恭喜你猜对了，只用了%d次" % counter )
        else:
            print("太笨了，猜了%d次还没猜对，游戏结束！" % counter)
        break
    elif number > answer :
        print("猜大了，再小一点")
    elif number < answer :
        print("猜小了，再大一点")