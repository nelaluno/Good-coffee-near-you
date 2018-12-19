import sys
from kivy.base import runTouchApp
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
root = Builder.load_string("""
#:import MapSource mapview.MapSource
<ZoomEdit@BoxLayout>:
    id:root.id
    Button:
        id: plus
        Image:
            source: "Data/Images/plus.jpg"
            allow_stretch: True
    Button:
        id: minus
        Image:
            source: "Data/Images/minus.jpg"
            allow_stretch: True
        
<Toolbar@StackLayout>:
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
<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size
RelativeLayout:
    MapView:
        id: mapview
        lat: 59.971483
        lon: 30.323102
        zoom: 50
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
        Button:
            text: 'sea'
        #Button:
        #    text: "Move to Lille, France"
        #    on_release: mapview.center_on(50.6394, 3.057)
        #Button:
        #    text: "Move to Sydney, Autralia"
        #    on_release: mapview.center_on(-33.867, 151.206)
        #Spinner:
        #    text: "mapnik"
        #    values: MapSource.providers.keys()
        #    on_text: mapview.map_source = self.text
    Toolbar:
        Label:
            text: "Longitude: {}".format(mapview.lon)
        Label:
            text: "Latitude: {}".format(mapview.lat)
    """)

runTouchApp(root)
#kwargs = {}
#if len(sys.argv) > 1:
#    kwargs["map_source"] = MapSource(url=sys.argv[1], attribution="")

#runTouchApp(MapView(**kwargs))
