import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, OptionProperty, StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.picker import MDThemePicker


Window.size = (400, 640) # (360, 600)

Builder.load_file('kvs/stages.kv')


class Stages(MDBoxLayout):
    '''A screen that display the stages.'''


class FrontPage(Screen):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }

    def default_on_action(self, *args):
        # print(app.root.ids.scr_mngr.current = 'search')
        print("IDS: ")
        print(self.ids)

    def callback(self, *args):
        print("CALLBACK: " + str(args))

    def invite_friends(self, *args):
        print("Invite Friends")
        

class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        # Initialize the application and return the root widget

        # Setting theme properties
        self.title = "Progress Exploration"
        self.theme_cls.theme_style = "Dark"
        self.icon = "images/accountpic.jpg"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Orange"
        self.theme_cls.accent_hue = "500"

        # Storing the screens in a list
        self.screens = [
            FrontPage(name="front_page"),
            #Stages(name="stages"),
        ]
        
        # Creating the screen manager,and setting the animation type to "fadetransition"
        self.screen_manager = WindowManager(transition=FadeTransition())

        # Adding screens to the screen manager
        for screen in self.screens:
            self.screen_manager.add_widget(screen)

        # Returning the screen manager
        return self.screen_manager

    def change_screen(self, screen):
        '''Change screen using the window manager.'''
        self.screen_manager.current = screen

    def show_theme_picker(self):
        '''Display a dialog window to change app's color and theme.'''
        theme_dialog = MDThemePicker()
        theme_dialog.open()


if __name__ == "__main__":
    MainApp().run()