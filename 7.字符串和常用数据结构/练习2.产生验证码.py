"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

Version: 0.1
Author: Ailin
"""

import random

def generate_code(code_len=4):
    """生成随机的验证码，默认为4"""
    all_charts = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for _ in range(code_len):
        key = random.randint(0,len(all_charts)-1)
        code += all_charts[key]
    return code

def main():
    print(generate_code(6))

if __name__ =="__main__":
    main()
