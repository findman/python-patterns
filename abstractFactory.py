#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta


class StandardFactory(object):
    '''这就是那个抽象工厂'''
    @staticmethod
    def get_factory(factory):
        '''根据参数查找对实际操作的工厂'''
        if factory == 'cat':
            return CatFactory()
        elif factory == 'dog':
            return DogFactory()
        raise TypeError('Unknow Factory')


class DogFactory(object):
    def get_pet(self):
        return Dog()


class CatFactory(object):
    def get_pet(self):
        return Cat()


# 可以认为dog和cat都是动物的一种，可以有个基类
class Pet(object):
    # ABCMeta会让这个类在注册后添加很多基础抽象基类，可以看[https://docs.python.org/3/library/abc.html]
    __metaclass__ = ABCMeta

    def eat(self):
        pass


# Dog应该做什么就在这里
class Dog(Pet):
    def eat(self):
        return 'Dog food...'


class Cat(Pet):
    def eat(self):
        return 'Cat food...'


if __name__ == "__main__":
    factory = StandardFactory.get_factory('cat')
    pet = factory.get_pet()
    print(pet.eat())

    factory = StandardFactory.get_factory('dog')
    pet = factory.get_pet()
    print(pet.eat())
