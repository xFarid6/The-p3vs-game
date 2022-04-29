import json
from datetime import datetime
from datetime import datetime as dt
from datetime import timedelta

import pyperclip
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import TwoLineListItem, ThreeLineListItem
from kivymd.uix.picker import MDThemePicker
# dichiarare una classe in una classe / loop infinito
from kivymd.uix.textfield import MDTextField

Window.size = (320, 600)

global wide_topic
global scoped_topic

wide_topic = "some string"
scoped_topic = "some string"


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):
    pass


class SearchPage(Screen):
    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        # MODIFY FROM HERE
        with open('conv_ideas.json', 'r') as file:
            data = json.load(file)
            for element in data:
                for topic in range(len(data[element])):
                    if search:
                        if text.lower() in data[element][topic]['name'].lower():
                            print(text)  # TODO: fix avoiding looking for the first letter
                            add_icon_item(data[element][topic]['name'])
                    else:
                        add_icon_item(data[element][topic]['name'])

    def on_start(self):
        self.screen.set_list_md_icons()

    def changeScreen(self, *args):
        self.parent.current = "main"


class SavedTopics(Screen):
    saved_topics = []

    def __init__(self, **kwargs):
        super(SavedTopics, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.loadSaves()
        print(self.saved_topics)

    def loadSaves(self):
        global wide_topic, scoped_topic

        for item in self.saved_topics:
            widget = ThreeLineListItem(text=item[1],
                                       tertiary_text=item[0].removesuffix("_topics"),
                                       theme_text_color="Custom",
                                       text_color=(0, 0, 0, 1))  # TODO: add short desc as secondary_text somehow
            widget.bind(on_release=self.changeScreenToScopedTopic)
            self.ids.listofsaves.add_widget(widget)
        for item in self.saved_topics:
            self.saved_topics.remove(item)

    def on_leave(self, *args):
        print("self.ids", self.ids)
        print("self.saved_topics", self.saved_topics)

    def changeScreen(self, *args):
        self.parent.current = "main"

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        scoped_topic = btn.text.lower()
        self.parent.current = "singletopic"
        SingleTopicWindow.request_from_saved_topics = True


class SingleTopicWindow(Screen):

    def __init__(self, **kwargs):
        super(SingleTopicWindow, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        with open('conv_ideas.json') as file:
            content = json.load(file)
        for topic in content[wide_topic]:
            if scoped_topic == topic['name']:
                self.ids.titlespace.title = str(topic['name'])
                self.ids.contentspace.text = str(topic['contenuto'])
                self.ids.questionspace.text = str(topic['domande_extra'])

        if self.request_from_saved_topics:
            print("reaching")
            self.ids.iconbutton.icon = "bookmark"

    request_from_saved_topics = False

    def on_enter(self, *args):
        global wide_topic, scoped_topic
        path = (wide_topic, scoped_topic)
        if path in SavedTopics.saved_topics:
            self.ids.iconbutton.icon = "bookmark"

    def on_leave(self, *args):
        self.request_from_saved_topics = False

    def changeScreen(self, *args):
        next_screen = wide_topic.removesuffix('_topics')
        self.parent.current = next_screen
        self.ids.iconbutton.icon = "bookmark-outline"

    def changeIcon(self, *args):
        global wide_topic, scoped_topic

        icons = ["bookmark", "bookmark-outline"]
        path = (wide_topic, scoped_topic)
        print(icons, self.ids.iconbutton.icon)

        if self.ids.iconbutton.icon == "bookmark-outline":
            self.ids.iconbutton.icon = "bookmark"
            if path not in SavedTopics.saved_topics:
                SavedTopics.saved_topics.append(path)
        elif self.ids.iconbutton.icon == "bookmark":
            self.ids.iconbutton.icon = "bookmark-outline"
            SavedTopics.saved_topics.remove(path)

        print(SavedTopics.saved_topics)
        '''
        if self.ids.iconbutton.icon in icons:
            icons.remove(self.ids.iconbutton.icon)
            self.ids.iconbutton.icon = icons[0]
            
        if self.ids.iconbutton.icon == "bookmark":
            if path not in SavedTopics.saved_topics:
                SavedTopics.saved_topics.append(path)
                print(SavedTopics.saved_topics)
        '''


class ConversationStarters(Screen):
    def __init__(self, **kwargs):
        super(ConversationStarters, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "doiknowyou_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False

    def changeScreen(self, *args):
        # now switch to the screen 1
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class HoverItem(MDIconButton, ThemableBehavior, HoverBehavior):
    '''Custom item implementing hover behavior.'''

    def on_enter(self, *args):
        '''The method will be called when the mouse cursor
        is within the borders of the current widget.'''

        self.md_bg_color = (1, 1, 1, 1)
        print("entering a MDIconButton")
        if self.hover_visible:
            print("the widget is visible")

    def on_leave(self, *args):
        '''The method will be called when the mouse cursor goes beyond
        the borders of the current widget.'''

        self.md_bg_color = self.theme_cls.bg_darkest


'''
class ActionButtons(MDBoxLayout):
    def __init__(self, **kwargs):
        super(ActionButtons, self).__init__(**kwargs)

        self.orientation = "horizontal"
        # self.size_hint_y = None
        # self.height = dp(45)
        self.adaptive_height = True
        self.padding = dp(0)
        self.md_bg_color = 0.224, 0.224, 0.224, 0.1

        self.bookmarked = []

        bookmark_btn = MDIconButton(icon="bookmark-outline", theme_text_color="Custom", pos_hint={'x': .2, 'y': .01},
                                    user_font_size="20sp")
        #bookmark_btn.bind(on_release=self.bookmark_controls)
        self.add_widget(bookmark_btn)


    def bookmark_controls(self, *args):
        global wide_topic, scoped_topic

        with open('conv_ideas.json') as file:
            content = json.load(file)

            if content.get(wide_topic):
                for item in content[wide_topic]:
                    if item['name'] == scoped_topic:
                        fav_path = (wide_topic, scoped_topic)
                        print(fav_path)
                        if fav_path not in self.bookmarked:
                            self.bookmarked.append(fav_path)
                            for fav in self.bookmarked:
                                print(fav)
                        else:
                            self.bookmark_btn.icon = "bookmark"

            # TODO: add button behavior when not saving
'''


class PhilosophyPage(Screen):

    # def on_enter(self, *args):
    # self.displayScreenThenLeave()
    def __init__(self, **kwargs):
        super(PhilosophyPage, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "filosofia_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False
            # print(state['name'], state["abbreviation"])
            # del state['area_codes']
            '''
            for i in range(20):
                self.ids.container.add_widget(
                    TwoLineListItem(text=f"Single-line item {i}")
                )
                '''

    def changeScreen(self, *args):
        # now switch to the screen 1
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class EconomicsPage(Screen):

    def __init__(self, **kwargs):
        super(EconomicsPage, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "economic_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False

    def changeScreen(self, *args):
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class PoliticsPage(Screen):

    def __init__(self, **kwargs):
        super(PoliticsPage, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "politica_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False

    def changeScreen(self, *args):
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class ClimatePage(Screen):

    def __init__(self, **kwargs):
        super(ClimatePage, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "climate_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False

    def changeScreen(self, *args):
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class TechPage(Screen):

    def __init__(self, **kwargs):
        super(TechPage, self).__init__(**kwargs)
        self.topics = dict()
        self.first_time_load = True

    def on_pre_enter(self, *args):
        global wide_topic
        global scoped_topic

        wide_topic = "tech_topics"
        key = 0
        with open('conv_ideas.json') as file:
            content = json.load(file)

        if self.first_time_load:
            for entry in content[wide_topic]:
                widget = TwoLineListItem(text=str(entry["name"]), secondary_text=str(entry['short_desc']),
                                         theme_text_color="Custom", text_color=(0, 0, 0, 1))
                widget.bind(on_press=self.changeScreenToScopedTopic)
                widget.id = entry['name']
                key += 1
                self.topics.update({widget.id: entry['name']})
                print(self.topics)
                self.ids.container.add_widget(widget)

            self.first_time_load = False

    def changeScreen(self, *args):
        self.parent.current = "main"
        # self.root.transition = SlideTransition(direction='right')  # see also FadeTransition

    def changeScreenToScopedTopic(self, btn):
        global scoped_topic
        print(btn, btn.id)
        scoped_topic = btn.id
        self.parent.current = "singletopic"
        print(wide_topic, scoped_topic)


class BigTopicSelectorCard(MDCard):
    def __init__(self, **kwargs):
        super(BigTopicSelectorCard, self).__init__(**kwargs)

    def on_enter(self):
        self.focus_behavior: True


class ContentNavigationDrawer(MDBoxLayout):
    pass


class LoadingWindow(Screen):
    pass


class MainPage(Screen):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.dialog = None

    def pasteMail(self):
        pyperclip.copy('santaclaus.vus@gmail.com')

        if not self.dialog:
            self.dialog = MDDialog(
                text="Dev mail has been copied to clipboard!",
                radius=[20, 7, 20, 7],
            )
        self.dialog.open()


class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)

    def changeScreen(self, *args):
        self.parent.current = "main"


class AccountPage(Screen):
    def __init__(self, **kwargs):
        super(AccountPage, self).__init__(**kwargs)

        self.first_time_enter = True
        self.nam3 = ObjectProperty(None)
        self.email = ObjectProperty(None)
        self.password = ObjectProperty(None)

    def on_pre_enter(self, *args):
        if self.first_time_enter:
            name = MDLabel(text="  Nome: ")
            card = MDCard()
            card.add_widget(name)
            self.nam3 = MDTextField(hint_text="invio per confermare", multiline=False,
                                    on_text_validate=lambda x: print(self.nam3.text))

            name1 = MDLabel(text="  Email: ")
            card1 = MDCard()
            card1.add_widget(name1)
            self.email = MDTextField(hint_text="invio per confermare", multiline=False,
                                     on_text_validate=lambda x: print(self.email.text))

            name2 = MDLabel(text="Crea una password: ")
            card2 = MDCard()
            card2.add_widget(name2)
            self.password = MDTextField(hint_text="invio per confermare", multiline=False,
                                        on_text_validate=lambda x: print(self.password.text))

            self.ids.accountlayout.add_widget(card)
            self.ids.accountlayout.add_widget(self.nam3)

            self.ids.accountlayout.add_widget(card1)
            self.ids.accountlayout.add_widget(self.email)

            self.ids.accountlayout.add_widget(card2)
            self.ids.accountlayout.add_widget(self.password)

            submit = MDRectangleFlatButton(text="CONFERMA", pos_hint={'center_x': 0.5, 'center_y': 0.38},
                                           size_hint=(.6, .3))
            submit.bind(on_release=self.createAccount)
            self.ids.floatspace.add_widget(submit)
        else:
            self.ids.accountlayout.clear_widgets()  # OMG I LOVE THIS FUNCTION
            self.ids.floatspace.clear_widgets()

            name = MDLabel(text="  Nome: ")
            card = MDCard(pos_hint={'center_x': 0.5, 'center_y': 0.9}, size_hint=(.85, .3))
            card.add_widget(name)
            nome = MDLabel(text=self.nam3.text)
            card.add_widget(nome)

            name1 = MDLabel(text="  Email: ")
            card1 = MDCard(pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint=(.85, .3))
            card1.add_widget(name1)
            email = MDLabel(text=self.email.text)
            card1.add_widget(email)

            self.ids.floatspace.add_widget(card)
            self.ids.floatspace.add_widget(MDLabel(text="   "))
            self.ids.floatspace.add_widget(card1)
            self.ids.floatspace.add_widget(MDLabel(text="   "))

    def on_enter(self, *args):
        pass

    def on_leave(self, *args):
        self.ids.accountlayout.clear_widgets()  # OMG I LOVE THIS FUNCTION
        self.ids.floatspace.clear_widgets()

    def createAccount(self, *args):
        if self.email.text and self.nam3.text and self.password.text:
            if "@" in self.email.text and "." in self.email.text:
                print("verified")
                self.first_time_enter = False

                # writing to file account.json
                data = {'account': []}
                string = "Creato il: " + str(dt.now())
                nome, email, password = "Nome: " + str(self.nam3.text), "Email: " + str(
                    self.email.text), "Password: " + str(self.password.text)
                data['account'].append({
                    'name': nome,
                    'email': email,
                    'password': password,
                    'created_on': string
                })
                print("saving shit")
                with open('account.json', 'w') as file:
                    json.dump(data, file, indent=2)

                self.popup = MDDialog(text="Ricarica per vedere i cambiamenti", radius=[8, 8, 8, 8],
                                      pos_hint={'center_x': .5, 'center_y': .5})
                self.popup.open()
            else:
                self.popup = MDDialog(text="Riempi i campi come si deve!", radius=[8, 8, 8, 8],
                                      pos_hint={'center_x': .5, 'center_y': .5})
                self.popup.open()
        else:
            self.popup = MDDialog(text="Riempi i campi come si deve!", radius=[8, 8, 8, 8],
                                  pos_hint={'center_x': .5, 'center_y': .5})
            self.popup.open()

    def changeScreen(self, *args):
        self.parent.current = "main"


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = FadeTransition()  # not actually setting the fade transition here


# KV = Builder.load_file("socrates.kv")


class SocratesApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_widget = Builder.load_file("socrates.kv")

    def build(self):
        # ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’,
        # ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’,
        # ‘Brown’, ‘Gray’, ‘BlueGray’.
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "600"
        # ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’
        self.theme_cls.theme_style = "Dark"  # TODO: implement light mode, change the font of the entire app    DONE

        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = 'Socrates'
        self.root_widget.transition = FadeTransition()  # Actually changing the transition
        #Window.borderless = True

        self.now = datetime.min
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text=self.now.strftime('%H:%M:%S'))

        return self.root_widget

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_label.text = self.now.strftime('%H:%M:%S')

    def show_theme_picker(self):
        '''Display a dialog window to change app's color and theme.'''
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def topicSuggestions(self, topic):
        pass
        # app.manager.current = topic


SocratesApp().run()

# buildozer init per regenerate each volta che si compile il file buildozer.spec;
# poi buildozer android debug
