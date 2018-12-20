import sys
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
root = Builder.load_string('''
#:kivy 1.10.1

#:import Label kivy.uix.label
#:import BoxLayout kivy.uix.boxlayout
#:import GridLayout kivy.uix.gridlayout
#:import CheckBox kivy.uix.checkbox
#:import Button kivy.uix.button

<HouseInfo@BoxLayout>:
    BoxLayout:
        Label:
            id: name
            #text: root.name
            italic: True
        Label:
            id: is_open
            #text: root.is_open
    BoxLayout:
        Label:
            text: "Время работы"
            italic: True
        Label:
            id: working
            #text: root.working
    GridLayout:
        cols: 3
        Label:
            text: "Латте"
        Label:
            id: latte_score
            #text: root.score#change
        Label:
            id: latte_price
            #text: root.price#change
        Label:
            text: "Капучино"
        Label:
            id: kapuchino_score
            #text: root.score#change
        Label:
            id: americano_price
            #text: root.price#change
        Label:
            text: "Американо"
        Label:
            id: kapuchino_score
            #text: root.score#change
        Label:
            id: americano_price
            #text: root.price#change
    Label:
        id: has_food_to_go''')


class HouseInfo(BoxLayout):
    #name = StringProperty('')
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(HouseInfo, self).__init__(**kwargs)
    def build(self):
        return root
    #def full(self,**kwargs):
    #    for _id in **kwargs:
    #        if _id in self,ids:
    #            setattr(root._id, kwargs[_id])
a = HouseInfo(name='House', is_open='открыто')
runTouchApp(a)
