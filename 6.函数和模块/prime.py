def is_prime(x):
    """判断是不是素数"""
    is_prime = True 
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 and x != i :
            is_prime = False
            break
    return is_prime
