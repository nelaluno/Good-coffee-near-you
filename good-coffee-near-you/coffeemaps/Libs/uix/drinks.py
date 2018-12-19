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

class D():
    def __init__(self, array):
        self.dropdown = DropDown()
        for index in range(len(array)):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
            btn = Button(text=array[index], size_hint_y=None, height=44)
            #for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

            # then add the button inside the dropdown
            self.dropdown.add_widget(btn)

        # create a big main button
        self.drinksbutton = Button(text='Выбрать кофе', size_hint=(None, None))
        self.drinksbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.drinksbutton, 'text', x))

def Drinks():
    def __init__(self, array):
        dropdown = DrinksDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
a = Builder.unload_file("drinks.kv")#Drinks()#['Ame', 'Cup', 'Lat'])
runTouchApp(a)
