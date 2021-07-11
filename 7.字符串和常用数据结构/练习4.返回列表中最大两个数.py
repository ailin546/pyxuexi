def max2(x=[1,8,6]):
    """
    返回传入列表中最大的两个元素
    """
    m1,m2 = (x[0],x[1]) if x[0]> x[1] else (x[1],x[0])
    for index in range(len(x)):
        if x[index]>m1 :
            m1,m2 = x[index],m1
        elif x[index]>m2:
            m2 = x[index]
    return m1,m2



if __name__ == "__main__":
    print(max2([1,8,6,5,45,24,100]))