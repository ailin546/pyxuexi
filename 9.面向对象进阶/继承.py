class Person(object):
    """ren"""

    def __init__(self,name,age):
        self._name = name 
        self._age = age 

    @property 
    def name(self):
        return self._name 
    @property 
    def age(self):
        return self._age 
    
    @age.setter 
    def age(self,age):
        self._age = age 
    
    def play(self):
        print("%s正在愉快的玩耍" % self._name)

    def watch_tv(self):
        if self._age > 18:
            print("%s正在看爱情动作片" % self._name)
        else:
            print("%s正在看小黄人" % self._name)

class Student(Person):
    """学生"""

    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade

    @property 
    def grade(self):
        return self._grade 
    @grade.setter 
    def grade(self,grade):
        self._grade = grade 
    def study(self,course):
        print("%s正在学习%s" % (self._name,course))

class Teacher(Person):
    """老师"""

    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title 
    @property
    def title(self):
        return self._title
    @title.setter 
    def title(self,title):
        self._title = title

    def teach(self,course):
        return "%s正在讲%s" % (self._name,course)

def main():
    s = Student("王大锤",15,"初三")
    s.study("数学")
    s.watch_tv()
    t = Teacher("罗浩",38,"专家")
    print(t.teach("python程序设计"))
    t.watch_tv()

if __name__ == "__main__":
    main()

