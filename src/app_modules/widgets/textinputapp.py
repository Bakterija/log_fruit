from text_editor import TextEditorPopup
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class TApp(App):
    def build(self):
        root = Label(text='Press "Enter" to open TextInput')
        Window.bind(on_key_down=self.on_key_down2)
        return root

    def on_key_down2(self, *args):
        if args[1] == 13:
            self.open_editor()

    def open_editor(self):
        popup = TextEditorPopup(text='')
        popup.open()


app = TApp()
app.run()
