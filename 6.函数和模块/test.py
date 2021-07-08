def foo(a):
    print(a)  # 200
    def bar():
        nonlocal a 
        a = 500
        print(a)
    bar()
    print(a)

if __name__ == '__main__':
    a = 100
    foo(a)
    print(a)  # 100
    foo(a)