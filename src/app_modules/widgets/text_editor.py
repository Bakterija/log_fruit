from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder


Builder.load_string('''
<TextEditor>:
    orientation: 'vertical'
    TextInput:
        id: input
        multiline: True
''')


class TextEditor(BoxLayout):
    pass


class TextEditorPopup(Popup):
    text = StringProperty()
    title = 'Text editor'

    def __init__(self, **kwargs):
        super(TextEditorPopup, self).__init__(**kwargs)
        self.content = TextEditor()

    def open(self, *args):
        super(TextEditorPopup, self).open(*args)
        self.content.ids.input.focus = True
        self.content.ids.input.text = self.text
