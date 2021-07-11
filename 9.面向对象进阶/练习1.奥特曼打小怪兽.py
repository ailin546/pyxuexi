from abc import ABCMeta,abstractmethod
from random import randint,randrange


class Fighter(object,metaclass=ABCMeta):

    __slots__ = ("_name","_hp")
    def __init__(self,name,hp):
        """初始化方法
        
        :param name:名字
        :param hp:生命值
        """
        self._name = name 
        self._hp = hp 
    @property
    def name(self):
        return self._name 
    @property
    def hp(self):
        return self._hp 
    
    @name.setter
    def name(self,name):
        self._name = name 
    @hp.setter 
    def hp(self,hp):
        self._hp = hp 
    @property 
    def alive(self):
        return self._hp > 0 
    @abstractmethod 
    def attack(self,other):
        """攻击
        :param other:被攻击的对象
        """
        pass

class Hero(Fighter):
    
    def __init__(self,name,hp=1000,mp=100):
        super().__init__(name,hp)
        self._mp = mp 
    
    @property
    def mp(self):
        return self._mp
    @mp.setter
    def mp(self,mp):
        self._mp = mp 
    def attack(self,other):
        other.hp -= randint(20,30)
        r = randint(5,10)
        self._mp += r
        print("%s通过普通攻击回复魔法%d点" %(self._name,self._mp))
    def huge_attack(self,other):
        """大招攻击
        :param other:被攻击对象
        """
        self._mp -= 50
        other.hp -= 100 if 100>3/4*other.hp else 3/4*other.hp
    def magic_attack(self,other):
        other.hp -= randint(40,50)
        self.mp -= 20
    def __str__(self):
        return "~~~%s奥特曼~~~\n" % self._name +\
            "生命值：%d\n" %self._hp + \
            "魔法值：%d\n" %self._mp 

class Bader(Fighter):
    """小怪兽"""
    def __init__(self,name,hp):
        super().__init__(name,hp)
    def attack(self,other):
        r = randint(20,30)
        other.hp -= r
        print("%s回击了%s,造成%d点伤害" %(self._name,other.name,r))


    def __str__(self):
        return "~~~%s小怪兽~~~\n" %self._name + \
            "生命值：%d\n" % self._hp

def is_any_alive(baders):
    for bader in baders:
        if bader.alive:
            return True 
    return False 

def select_bader(baders):
    baders_len = len(baders)
    while True:
        index = randrange(baders_len)
        bader = baders[index]
        if bader.alive:
            return bader
def display_info(hero,baders):
    print(hero)
    for bader in baders:
        print(bader,end='')

def main():
    u = Hero('爱林',2000,100)
    m1 = Bader('金钱',200)
    m2 = Bader("欲望",300)
    m3 = Bader("生活",600)
    ms = [m1,m2,m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(u.alive)
        print(is_any_alive(ms))
        print("------第%d回合！------"%fight_round)
        m = select_bader(ms)
        if u.mp > 100:
            print("%s使用大招攻击了%s" %(u.name,m.name))
            u.huge_attack(m)
        elif u.mp >20:
            print("%s使用技能攻击了%s" %(u.name,m.name))
            u.magic_attack(m)
        else:
            u.attack(m)
        for bader in ms:
            if bader.alive:
                bader.attack(u)
        display_info(u,ms)
        fight_round += 1
    print("\n======战斗结束======\n")
    if u.alive:
        print("%s获得了胜利！"% u.name)
    else:
        print("小怪兽获得了胜利")

if __name__ == "__main__":
    main()
