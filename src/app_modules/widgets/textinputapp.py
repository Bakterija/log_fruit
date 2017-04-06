from text_editor import TextEditorPopup
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<BoxxLayout>:
    orientation: 'vertical'
    TextInput:
        id: textwidget
        size_hint: 1, 0.9
        focus: True
    Button:
        size_hint: 1, 0.1
        on_release: textwidget = False
''')


class BoxxLayout(BoxLayout):
    pass


class TApp(App):
    def build(self):
        root = BoxxLayout()
        # root = Button(text='Press "Enter" to open TextInput', on_release=self.open_editor)
        Window.bind(on_key_down=self.on_key_down2)
        return root

    def on_key_down2(self, *args):
        if args[1] == 13:
            self.open_editor()

    def open_editor(self, *args):
        popup = TextEditorPopup(text='')
        popup.open()


app = TApp()
app.run()
