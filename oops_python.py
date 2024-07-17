# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:51:11 2021

@author: INDHRNA
"""

class Dog:
    pass

class Dogs:
    species = 'canis familiaris'
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def description(self):
        return '{} is {} years old'.format(self.name,self.age)
    def __str__(self):
        return '{} is {} years old'.format(self.name,self.age)
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)
dogy = Dogs('street',4,'dausch')
dggy = Dogs('pet', 6, 'lowbark')
a='ssddee'
