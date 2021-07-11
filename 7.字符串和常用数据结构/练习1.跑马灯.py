"""
在屏幕上显示跑马灯文字

Version: 0.1
Author: Ailin
"""
import time
import os 

def main():
    content = '北京欢迎你，为你开天辟地……'
    while True:
        #清理屏幕输出
        os.system('cls')
        #os.system('clear')是清屏命令，windows中为os.system('cls')
        print(content)
        #休眠200ms
        time.sleep(0.02)
        content = content[1:] + content[0]

if __name__ =='__main__':
    main()