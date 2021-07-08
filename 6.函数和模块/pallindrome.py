def is_pallindrome(x):
    """判断是不是回文数
    is_pallindrome = True
    i = 1
    num = x 
    while num >= 10:
        num /= 10
        i += 1
    for j in range(i):
        if x // (10**j)%10 != x // (10**(i-j-1))%10:
            is_pallindrome = False
            break
    return is_pallindrome
    """
    total = 0
    temp = x 
    while temp > 0 :
        total = total*10 + temp % 10
        temp //= 10
    return x == total



