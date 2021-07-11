def triangles(x):
    """杨辉三角
    :param x:打印多少行
    """
    yh = [[]] *x
    for row in range(len(yh)):
        yh[row]=[None]*(row+1)
        for col in range(len(yh[row])):
            if col ==0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col]+yh[row-1][col-1]
            print(yh[row][col],end='\t')
        print()
def main():
    print(triangles(6))

if __name__ =="__main__":
    main()
