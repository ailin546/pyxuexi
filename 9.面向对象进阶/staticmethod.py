from math import sqrt 

class Triangle(object):

    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c

    @staticmethod 
    def is_valid(a,b,c):
        return a+b>c and a+c >b and b+c>a 

    def perimeter(self):
        return self.a +self.b +self.c 

    def area(self):
        p = self.perimeter()/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

def main():
    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.area())
    else:
        print("不能生成三角形")
if __name__ == "__main__":
    main()