from math import sqrt 

class Point(object):

    def __init__(self,x=0,y=0):
        """
        :param x:横坐标
        :param y:纵坐标
        """
        self.x = x
        self.y = y
    def move_to(self,x,y):
        """
        移动到指定位置
        :param x:要移动到的横坐标
        :param y:要移动到的纵坐标
        """
        self.x = x
        self.y = y
    def move_by(self,dx,dy):
        """移动指定的增量
        
        :param dx:横坐标的增量
        :param dy:纵坐标的增量
        """
        self.x += dx 
        self.y += dy

    def distance(self,other):
        """
        计算与另一点的距离
        :param x:点的横坐标
        :param y:点的纵坐标
        """
        return sqrt((self.x - other.x)**2 +(self.y - other.y)**2)
    def __str__(self):
        return '(%s,%s)' %(str(self.x),str(self.y))

def main():
    p1 = Point(6,26)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,8)
    print(p1.distance(p2))
    p1.move_to(-6,6)
    print(p1)
if __name__ =="__main__":
    main()