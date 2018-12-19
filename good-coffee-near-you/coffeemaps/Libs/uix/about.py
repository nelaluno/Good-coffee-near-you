﻿#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# about.py
#

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from .custombutton import CustomButton

class About(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    text_license = StringProperty("Clean Master")
    about_background = ListProperty(
        [0.7294117647058823, 0.7686274509803922, 0.8470588235294118])

    Builder.load_file("Libs/uix/kv/about.kv")
    """Макеты интерфейса"""

    def __init__(self, **kvargs):
        super(About, self).__init__(**kvargs)
        self.create_button_share(self.ids.box_share)

    def create_button_share(self, box_share):
        """Добавляет кнопки меню share в макет.

        :type box_share: <'kivy.weakproxy.WeakProxy'>
        :param box_share: <'kivy.uix.gridlayout.GridLayout'>

        """

        about_items_share = {
            "Share this app": "Data/Images/about_share.png",
            "Like us on Facebook": "Data/Images/about_facebook.png",
            "Join our beta testing group": "Data/Images/google_plus.png",
            "Help us with localization": "Data/Images/about_localization.png",
            "For Business Cooperation": "Data/Images/skype_icon.png"}

        for name_item in about_items_share.keys():
                box_share.add_widget(
                    CustomButton(icon_load="Data/Images/previous_image.png",
                                 icon=about_items_share[name_item],
                                 button_text=name_item, button_height=45,
                                 icon_height=25))
