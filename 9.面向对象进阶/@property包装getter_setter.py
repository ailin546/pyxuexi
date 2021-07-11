"""
属性以单下划线开头，暗示属性是受保护的，不建议直接访问，如果想访问属性可以通过
属性的getter（访问器）和setter（修改器），可以使用@property包装器来包装
getter和setter方法。
"""
class Person(object):

    def __init__(self,name,age):
        self._name = name 
        self._age = age 

    #访问器 - getter方法
    @property 
    def name(self):
        return self._name 

    @property 
    def age(self):
        return self._age

    #修改器 - setter方法
    @age.setter 
    def age(self,age):
        self._age = age 
    @name.setter 
    def name(self,name):
        self._name = name 

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋。" % self._name)
        else:
            print("%s正在玩斗地主" % self._name)
def main():
    person = Person('王大锤',13)
    person.play()
    person.age = 22
    person.play()
    person.name = "白元芳"
    person.play()

if __name__ == "__main__":
    main()