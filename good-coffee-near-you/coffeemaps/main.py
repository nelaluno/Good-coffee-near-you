#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# main.py
#
# Точка входа в приложение. Запускает основной программный код program.py.
# В случае ошибки, выводит на экран окно с ее текстом.
#

from __future__ import print_function

import os
import sys
import traceback

try:
    import kivy
    kivy.require("1.10.1")

    from kivy.app import App
    from kivy.config import Config

    # Указываем пользоваться системным методом ввода, использующимся на
    # платформе, в которой запущенно приложение.
    Config.set("kivy", "keyboard_mode", "system")

    # Activity баг репорта.
    from Libs.uix.bugreporter import BugReporter
except Exception:
    print("\n\n{}".format(traceback.format_exc()))
    sys.exit(1)

__version__ = "0.0.1"

def main():
    app = None

    try:
        from coffeemap  import CoffeeMap # основной класс программы

        # Запуск приложения.
        app = CoffeeMap()
        app.run()
    except Exception as exc:
        print(traceback.format_exc())
        traceback.print_exc(file=open("{}/error.log".format(
            os.path.split(os.path.abspath(sys.argv[0]))[0]), "w"))

        if app:  # очищаем экран приложения от всех виджетов
            app.start_screen.clear_widgets()

        class Error(App):
            """Выводит экран с текстом ошибки."""

            def callback_report(self, *args):
                """Функция отправки баг-репорта"""

                try:
                    import webbrowser
                    import six.moves.urllib

                    txt = six.moves.urllib.parse.quote(
                        self.win_report.txt_traceback.text.encode(
                            "utf-8"))
                    url = "https://github.com/HeaTTheatR/KivyCleanMasterDemo" \
                          "/issues/new?body=" + txt
                    webbrowser.open(url)
                except Exception:
                    sys.exit(1)

            def build(self):
                self.win_report = BugReporter(
                    callback_report=self.callback_report, txt_report=str(exc),
                    icon_background="Data/Images/logo.png")
                return self.win_report

        Error().run()

if __name__ in ("__main__", "__android__"):
    main()
