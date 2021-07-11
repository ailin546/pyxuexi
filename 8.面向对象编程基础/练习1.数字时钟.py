from time import sleep 
import os

class Clock(object):
    """数字时钟"""
    def __init__(self,hour=0,month=0,second=0):
        """
        :param hour:时
        :param month:分
        :param second:秒
        """
        self.hour = hour 
        self.month = month 
        self.second = second 
    
    def run(self):
        """走字"""
        while True:
            
            sleep(1)

            self.second += 1
            os.system("cls")
            if self.second == 60:                
                self.second = 0
                self.month +=1 
                if self.month == 60:
                    self.month = 0
                    self.hour += 1
                    if self.hour == 24:
                        self.hour = 0
            print("现在是%d时%d分%d秒"% (self.hour,self.month,self.second))
    def show(self):
        return "现在是%d时%d分%d秒"% (self.hour,self.month,self.second)
            
def main():
    print(Clock(16,59,50).show())

if __name__ =="__main__":
    main()


