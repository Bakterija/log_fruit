from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_string('''
<TextEditor>:
    orientation: 'vertical'
    TextInput:
        id: input
        multiline: True
        font_size: logview_font_size
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
        self.content.ids.input.text = self.text
        Clock.schedule_once(self.focus_textinput, 0)

    def focus_textinput(self, *args):
        self.content.ids.input.focus = True
