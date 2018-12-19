#import gmaps
#from kivy.app import App


#from kivy.garden.mapview import MapView
#from kivy.app import App

#class MapViewApp(App):
#    def build(self):
#        mapview = MapView(zoom=20, lat=59.971530, lon=30.323057)
#        return mapview

#a=MapViewApp()
#a.run()
from kivy.base import runTouchApp
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#kw ={}
root = Builder.load_file("maptry.kv")

runTouchApp(root)
