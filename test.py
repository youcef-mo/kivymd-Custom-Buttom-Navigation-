from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFloatingActionButtonSpeedDial, MDRectangleFlatButton, MDFloatingActionButton, MDFillRoundFlatButton
import kivymd_extensions.akivymd
from kivymd_extensions.akivymd.uix.bottomnavigation2 import Button_Item
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
Window.size = (350, 580)

KV = '''
#:import NoTransition kivy.uix.screenmanager.NoTransition
<On_active_button@Button_Item>
    icon_color: 
        app.theme_cls.text_color if not root.selected_item \
        else (1, 1, 1, 1)       
    text_color:
        app.theme_cls.text_color if not root.selected_item \
        else (1, 1, 1, 1) 
    button_bg_color:
        app.theme_cls.text_color if root.selected_item \
        else (0, 1, 1, 0.1)
    mode: "color_on_normal"
    badge_disabled: True

MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    ScreenManager:
        id : scr
        transition: NoTransition()

        MDScreen:
            id : scr1
            md_bg_color: 0, 0, 1, 1
            name: "home"
            MDLabel:
                text: "Home"
                pos_hint: {"center_x": .5, "center_y": .5}
        MDScreen:
            id : scr2
            md_bg_color: 1, 0, 1, 1
            name: "search"
            MDLabel:
                text: "Search"
                pos_hint: {"center_x": .5, "center_y": .5}
        MDScreen:
            id : scr3
            md_bg_color: 0, 1, 1, 1
            name: "favorite"
            MDLabel:
                text: "Favorite"
                pos_hint: {"center_x": .5, "center_y": .5}
        MDScreen:
            id : scr4
            md_bg_color: 1,1,0,1
            name: "profile"
            MDLabel:
                text: "Profile"
                pos_hint: {"center_x": .5, "center_y": .5}
    
    NavBar:
        id: navbar
        size_hint: .95, .09
        pos_hint: {"center_x": .5, "center_y": .1}
        elevation: 15
        md_bg_color: 1,1,1,1
        radius: [25]
        width: self.width
        
        On_active_button:
            text: "Home"
            icon: "home-circle-outline"
            
            pos_hint: {"center_x": .13, "center_y": .5}
            button_width: navbar.width / 4
            on_release:
                scr.current = "home"
                app.on_touch(self)
                          
        On_active_button:
            text: "search"
            icon: "compass"
            
            pos_hint: {"center_x": .37, "center_y": .5}
            button_width: navbar.width / 4
            on_release:
                scr.current = "search"
                app.on_touch(self)
                
        On_active_button:
            text: "Likes"
            icon: "heart-circle-outline"
            
            pos_hint: {"center_x": .62, "center_y": .5}
            button_width: navbar.width / 4
            on_release:
                scr.current = "favorite"
                app.on_touch(self)
        
        On_active_button:
            text: "Me"
            icon: "account-circle-outline"
            
            pos_hint: {"center_x": .87, "center_y": .5}
            button_width: navbar.width / 4
            on_release:
                scr.current = "profile"
                app.on_touch(self)

'''

class On_active_button(Button_Item):

    selected_item = BooleanProperty(False)        
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
            
        return super().on_touch_down(touch)  

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class MDFloatlayout():
    pass

class Example(MDApp):
    title = "Example Animation Card"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(KV)

    def on_touch(self, instance):
        pass
        #for instance in self.root.ids.scr.children:
            #current_id = list(self.root.ids.values()).index(instance)
            
Example().run()