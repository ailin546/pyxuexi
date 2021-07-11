def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    """
    return year % 4 == 0 and year % 100 !=0 or year % 400 ==0

def which_day(year,month,date):
    """计算是这一年的第几天
    
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    if is_leap_year(year):
        days_of_month=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_of_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    total += date
    return total

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()