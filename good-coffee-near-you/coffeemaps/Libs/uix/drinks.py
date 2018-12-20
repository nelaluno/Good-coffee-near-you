#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# drinks.py
#https://kivy.org/doc/stable/api-kivy.uix.dropdown.html

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.lang import Builder
from drinksdropdown import DrinksDropDown

class Drinks():
    def __init__(self, array):
        dropdown = DrinksDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
a = Builder.load_file("drinks.kv")#Drinks()#['Ame', 'Cup', 'Lat'])
print(a)
runTouchApp(a)
