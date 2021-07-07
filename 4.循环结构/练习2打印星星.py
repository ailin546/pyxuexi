"""
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
打印三角形图案

version:0.1
Author: Ailin
Date: 2021-7-6
"""
row = int(input("请输入行数:"))
for x in range(1,row+1):
    for y in range(x):
        print("*",end = "")
    print("")
print("\n")
for x in range(row):
    for y in range(row):
        if y < row-x-1:
            print(" ",end="")
        else:
            print("*",end="")
    print("")
print("\n")

for x in range(row):
    for y in range(2 *row -1):
        if y < row - x -1:
            print(" ",end="")
        elif y < row + x :
            print("*",end = "")
        else:
            print(" ",end="")
    print("")