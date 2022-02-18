from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExemple(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='A')
        b2 = Button(text='B')
        l1 = Label(text="groink")

        self.orientation='vertical'
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(l1)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()