# -*- coding: utf-8 -*-
#
# searchlayout.py
#
# Поле для поиска
#

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.actionbar import ActionItem
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.base import runTouchApp


class SearchLayout(BoxLayout):
    def __init__(self):
        id = StringProperty("")
        setattr(root.mincost, 'text', str(100))
        setattr(root.maxcost, 'text', str(200))
a = Builder.load_file( "Libs\uix\kv\searchlayout.kv")#SearchLayout()
runTouchApp(a)
