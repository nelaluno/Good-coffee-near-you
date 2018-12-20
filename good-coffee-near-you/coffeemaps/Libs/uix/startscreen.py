import sys
from kivy.base import runTouchApp
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
root = Builder.load_string('''
# -*- coding: utf-8 -*-
#:kivy 1.10.1
#:import SearchLayout .searchlayout
#:import HouseInfo .houseinfo 
#:import MapSource mapview.MapSource

<ScoreDropDown@DropDown>:
    Slider:
        id: score
        orientation: "vertical"
        min: 0
        max: 5
        value: 3
        value_track: True
        #value_track_color: [0, 0, 1, 0.5]
        #on_touch_up:
        step: 0.1
        on_value: root.select(abs(score.value))

<SearchLayout@BoxLayout>:
    id: root.id
    orientation: "vertical"
    padding: 10
    spacing:5
    #color: 
    Label:
        text: 'Параметры поиска'
        fint_size: '30sp'
        size_hint: (1, 0.2)
    Spinner:
        id: root.drinks
        text: "Выбрать кофе"
        values: "Капучино", "Латте", "Американо", "Любой кофе"
        size_hint: (1, 0.2)
        #size:
    GridLayout:
        cols:3
        Label:
            size_hint: (1, 0.1)
        Label:
            size_hint: (1, 0.1)
        Label:
            size_hint: (1, 0.1)
        Label:
            text:'Приоритет'
            size_hint: (1, 0.1)
        Label:
            size_hint: (0.2, 0.2)
            text: "Цена:"
        BoxLayout:
            TextInput:
                id: mincost
                size_hint: 1, 0.2
                multiline: False
                text: "min"
            TextInput:
                id: maxcost
                size_hint: 1, 0.2
                multiline: False
                text: "max"
        CheckBox:
            size_hint: (0.5, 0.2)
            id: cost_priority
            group: 'priority'
        Label:
            text: 'Минимальный рейтнг:'
        Button:
            id:scorebutton
            text: "3"
            on_release: score_drop_down.open()
        ScoreDropDown:
            id: score_drop_down
            on_select: lambda instance, x: setattr(scorebutton, 'text', x)
        CheckBox:
            size_hint: (0.5, 0.2)
            id: score_priority
            group: 'priority'
    GridLayout:
        cols:4
        size_hint: 1, 0.2
        Label:
            text: "Открыто"
            size_hint: (0.2, 0.5)
        CheckBox:
            id: is_open
            active: True
            size_hint: (0.2, 0.2)
        Label:
            size_hint: (0.5, 0.5)
            text: "Есть еда с собой"
        CheckBox:
            size_hint: (0.2, 0.2)
            id: has_food_to_go
    Button:
        text: "Добавить новую кофейню"
        #on_release: 
    Button:
        text: "Изменить информацию о кофейне"
        #on_release:
<ZoomEditor@BoxLayout>:
    id:root.id
    Button:
        id: plus
        Image:
            source: "Data\Images\plus.jpg"
            allow_stretch: True
        on_press: editzoom(-5)
    Button:
        id: minus
        Image:
            source: "Data\Images\minus.jpg"
            allow_stretch: True
        on_press: editzoom(+5)
        
<Toolbar@Layout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'
    canvas:
        Color:
            rgba: .2, .2, .2, .2
        Rectangle:
            pos: self.pos
            size: self.size
    
            
RelativeLayout:
    MapView:
        id: mapview
        lat: 59.971483
        lon: 30.323102
        zoom: 30
        #size_hint: .5, .5
        #pos_hint: {"x": .25, "y": .25}
        #on_map_relocated: mapview2.sync_to(self)
        #on_map_relocated: mapview3.sync_to(self)
        #MapMarker:
        #    id: user
        #    lat: 59.971483
        #    lon: 30.323102
        #MapMarker:
        #    lat: -33.867
        #    lon: 151.206
    Toolbar:
        top: root.top
        GridLayout:
            cols: 2
            Button:
                Imagine:
                    source: "Data\Images\searching.jpg"
                    allow_stretch: False
                on_press: searching.open
        DropDown:
            id: searching
            Widget:
                SearchLayout:
            on_select: self.dismiss()

<StartScreen>
    ActionBar:
        id: action_bar
        ActionView:
            ActionPrevious:
                id: action_previous
                with_previous: True
                on_press: root.events_callback("on_previous")
            ActionOverflow:
                id: action_overflow
    # Менеджер экранов.
    ScreenManager:
        id: screen_manager
        # Текущий стартовый экран.
        Screen:
            id: start
            RelativeLayout:
                MapView:
                    id: mapview
                    lat: 59.971483
                    lon: 30.323102
                    zoom: 30
                    #size_hint: .5, .5
                    #pos_hint: {"x": .25, "y": .25}
                    #on_map_relocated: mapview2.sync_to(self)
                    #on_map_relocated: mapview3.sync_to(self)
                    #MapMarker:
                    #    id: user
                    #    lat: 59.971483
                    #    lon: 30.323102
                    #MapMarker:
                    #    lat: -33.867
                    #    lon: 151.206
                Button:
                    size_hint_y: None
                    height: '48dp'
                    padding: '4dp'
                    spacing: '4dp'
                    top: root.top
                    GridLayout:
                        cols: 2
                        Button:
                            Imagine:
                                source: "Data\Images\searching.jpg"
                                allow_stretch: False
                            on_release: menu.open(searching)
                DropDown:
                    id: menu
                    SearchLayout:
                        id: searching
                        on_select: self.dismiss()
                    PageLayout:
                        id: results
                        Label:
                            text: '1'
                        Label:
                            text: '2'
                            ''')

#:kivy 1.10.1
#:import SearchLayout .searchlayout
#:import HouseInfo .houseinfo 
#:import MapSource mapview.MapSource

class ScoreDropDown(DropDown):
    pass

class SearchLayout(BoxLayout):
    #root.drinks Spinner
    #values: "Капучино", "Латте", "Американо", "Любой кофе"
    #mincost TextInput
    #maxcost TextInput:
    #cost_priority CheckBox 'priority'
    #scorebutton Button score_drop_down.open()
    #score_drop_down on_select: lambda instance, x: setattr(scorebutton, 'text', x)
    #score_priority CheckBox 'priority'
    #is_open CheckBox
    #has_food_to_go CheckBox
    #Button "Поиск" on_release
    #Button "Добавить новую кофейню" on_release
    #Button "Изменить информацию о кофейне" on_release
    pass

class ZoomEditor(BoxLayout, Widget):
    #plus on_press: editzoom(-5)
    #minus on_press: editzoom(+5)
    pass
        
class Toolbar(Layout):
    pass

    
RelativeLayout:
    MapView:
        id: mapview
        lat: 59.971483
        lon: 30.323102
        zoom: 30
        #size_hint: .5, .5
        #pos_hint: {"x": .25, "y": .25}
        #on_map_relocated: mapview2.sync_to(self)
        #on_map_relocated: mapview3.sync_to(self)
        #MapMarker:
        #    id: user
        #    lat: 59.971483
        #    lon: 30.323102
        #MapMarker:
        #    lat: -33.867
        #    lon: 151.206
    Toolbar:
        top: root.top
        GridLayout:
            cols: 2
            Button:
                Imagine:
                    source: "Data\Images\searching.jpg"
                    allow_stretch: False
                on_press: searching.open
        DropDown:
            id: searching
            Widget:
                SearchLayout:
            on_select: self.dismiss()

<StartScreen>
    ActionBar:
        id: action_bar
        ActionView:
            ActionPrevious:
                id: action_previous
                with_previous: True
                on_press: root.events_callback("on_previous")
            ActionOverflow:
                id: action_overflow
    # Менеджер экранов.
    ScreenManager:
        id: screen_manager
        # Текущий стартовый экран.
        Screen:
            id: start
            RelativeLayout:
                MapView:
                    id: mapview
                    lat: 59.971483
                    lon: 30.323102
                    zoom: 30
                    #size_hint: .5, .5
                    #pos_hint: {"x": .25, "y": .25}
                    #on_map_relocated: mapview2.sync_to(self)
                    #on_map_relocated: mapview3.sync_to(self)
                    #MapMarker:
                    #    id: user
                    #    lat: 59.971483
                    #    lon: 30.323102
                    #MapMarker:
                    #    lat: -33.867
                    #    lon: 151.206
                Button:
                    size_hint_y: None
                    height: '48dp'
                    padding: '4dp'
                    spacing: '4dp'
                    top: root.top
                    GridLayout:
                        cols: 2
                        Button:
                            Imagine:
                                source: "Data\Images\searching.jpg"
                                allow_stretch: False
                            on_release: menu.open(searching)
                DropDown:
                    id: menu
                    SearchLayout:
                        id: searching
                        on_select: self.dismiss()
                    PageLayout:
                        id: results
                        Label:
                            text: '1'
                        Label:
                            text: '2'
runTouchApp(root)
#kwargs = {}
#if len(sys.argv) > 1:
#    kwargs["map_source"] = MapSource(url=sys.argv[1], attribution="")

#runTouchApp(MapView(**kwargs))
