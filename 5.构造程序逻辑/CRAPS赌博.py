"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

我们设定初始1000000赌注，游戏结束为玩家输光

Version: 0.1
Author: Ailin
"""
import random

money = 1000000
num = 0

while money > 0:
    is_game = input("是否继续游戏？继续请输入Y")
    if "Y" in is_game or "y" in is_game:
        num += 1
        point_1 = random.randint(1,6)
        point_2 = random.randint(1,6)
        fund = float(input("请输入下注金额："))
        if fund > money :
            print("您的资金不足，请重新输入")
            continue;
        first = point_1 + point_2 
        print("第一个筛子为%d,第二个为%d，总和为%d" % (point_1,point_2 , first ))
        if point_1 + point_2 == 7 or point_1 +point_2 == 11:
            money += fund 
            print("恭喜你胜利了！,剩余金额为%.2f" % money )
            continue
        elif point_1 + point_2 ==2 or point_1 + point_2 ==3 or point_1 +point_2 ==12:
            money -= fund 
            print("You lose,剩余金额%.2f" % money )
            continue;
        else:
            print("未分胜负，将进入第二轮")
            while True:
                point_1 =random.randint(1,6)
                point_2 = random.randint(1,6)
                second = point_1 + point_2 
                print("第一个筛子为%d,第二个为%d，总和为%d" % (point_1,point_2 , second ))
                if second == 7:
                    money -= fund 
                    print("You lose,剩余金额为%.2f" % money)
                    break
                elif second == first:
                    money += fund 
                    print("恭喜你胜利了！,剩余金额为%.2f" % money)
                    break
                else:
                    print("无结果，将重新投掷")




    else:
        print("游戏结束，您共玩了%d次，剩余资金为%d" % (num,money ))
        break
print("游戏结束，您共玩了%d次，剩余资金为%d" % (num,money ))