import pallindrome
import prime
if __name__ =="__main__":
    num = int(input("请输入正整数："))
    if pallindrome.is_pallindrome(num) and prime.is_prime(num):
        print("%d是回文质数" % num)
    else:
        print("%d不是回文质数" % num)