from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):  #抽象基类
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod       #抽象化 无法调用
    def make_voice(self):
        """发出声音"""
        print("111")
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Pet('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()