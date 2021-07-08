def gys(x,y):
    if x>y:
        x,y =y,x 
    for i in range(x,0,-1):
        if y%i ==0 and x % i == 0:
            return i
            break

def gbs(x,y):
    return x*y // gys(x,y)

print(gbs(12,20))