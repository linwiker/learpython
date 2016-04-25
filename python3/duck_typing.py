#/usr/bin/env python
# -*- coding: utf-8 -*-
_metaclass_=type
class Duck:
    def quack(self):
        print("Quaaaaaaack")
    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the group and show it.")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()