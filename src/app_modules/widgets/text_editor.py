from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_string('''
<TextEditor>:
    orientation: 'horizontal'
    ScrollView:
        id: scroller
        bar_width: cm(0.5)
        TextInput:
            id: input
            size_hint: 1, None
            height: self.minimum_height if root.height < self.minimum_height else root.height
            multiline: True
            font_size: logview_font_size
            on_cursor: root.on_cursor(args[1])
            on_cursor_row: root.on_cursor_row(args[1])
''')


class TextEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(TextEditor, self).__init__(**kwargs)

    def on_cursor(self, value):
        pass

    def on_cursor_row(self, value):
        max_lines = int(self.ids.input.height / self.ids.input.line_height)
        prc = value / max_lines
        # print (value, max_lines, prc)
        self.ids.scroller.scroll_y = 1.0 - prc


class TextEditorPopup(Popup):
    text = StringProperty()
    title = 'Text editor'

    def __init__(self, **kwargs):
        super(TextEditorPopup, self).__init__(**kwargs)
        self.content = TextEditor()
        self.size_hint = (0.9, 0.9)

    def open(self, *args):
        super(TextEditorPopup, self).open(*args)
        self.content.ids.input.text = self.text
        Clock.schedule_once(self.focus_textinput, 0)

    def focus_textinput(self, *args):
        self.content.ids.input.focus = True
