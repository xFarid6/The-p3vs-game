import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (360, 600)


class WindowManager(ScreenManager):
    pass


class MessageScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        pass


if __name__ == "__main__":
    MainApp().run()