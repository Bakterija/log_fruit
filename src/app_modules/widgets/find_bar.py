from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.stencilview import StencilView


Builder.load_string('''
<FindBar>:
    canvas.before:
        Color:
            rgba: col_dgrey
        Rectangle:
            size: self.size
            pos: self.pos

    TextInput:
        size_hint: 1, 0.5
    TextInput:
        size_hint: 1, 0.5
''')


class FindBar(StackLayout, StencilView):

    def __init__(self, **kwargs):
        super(FindBar, self).__init__(**kwargs)
