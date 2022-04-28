import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


Window.size = (360, 600)


class WindowManager(ScreenManager):
    pass


class MessageScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        # Initialize the application and return the root widget

        # Setting theme properties
        self.title = "Progress Exploration"
        self.theme_cls.theme_style = "Dark"
        # self.icon = "data/icon.png"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.accent_hue = "500"

        # Storing the screens in a list
        self.screens = [
            MessageScreen(name="message_screen"),
        ]
        
        # Creating the screen manager,and setting the animation type to "fadetransition"
        self.screen_manager = WindowManager(transition=FadeTransition())

        # Adding screens to the screen manager
        for screen in self.screens:
            self.screen_manager.add_widget(screen)

        # Returning the screen manager
        return self.screen_manager


if __name__ == "__main__":
    MainApp().run()