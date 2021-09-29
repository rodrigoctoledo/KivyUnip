from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class PopUpApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text="Hello! Thank you.")

        # popup widget
        self.popup = Popup( title="Popup Demo", content=(Label( text="Hello! Thank you." )), size_hint=(0.3, 0.3) )

        # class attributes
        self.cols = 2

        # Button Widget To Open Popup
        self.open_btn = Button(text="Open Popup",  size_hint=(0.5, None), height="60dp")
        self.open_btn.bind(on_press=self.open_popup)
        self.add_widget( self.open_btn )

        # Button Widget To Close Popup
        self.close_btn = Button(text="close Popup", size_hint=(0.5, None), height="60dp" )
        self.close_btn.bind( on_press=self.close_popup)
        self.add_widget( self.close_btn )

    def open_popup(self, instance):
        local_popup = self.popup.open()
        return local_popup

    def close_popup(self, instance):
        local_close_popup = self.popup.dismiss()
        return local_close_popup


class ExecuteApp(App):
    def build(self):
        return PopUpApp()


if __name__ == "__main__":
    ExecuteApp().run()