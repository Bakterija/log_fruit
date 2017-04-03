from kivy.properties import (
    ListProperty, BooleanProperty, StringProperty, ObjectProperty)
from .databox.databox import DataBox, DataView
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from time import time, sleep


class TabHolder(BoxLayout):
    current_selection = ObjectProperty()
    current_selection_text = StringProperty()
    max_children = 10

    def __init__(self, **kwargs):
        super(TabHolder, self).__init__(**kwargs)
        for x in range(3):
            self.add_filter(str(x))

    def add_filter(self, text='', select=True):
        if len(self.children) < self.max_children:
            new = FilterTab(text=text, selected=select)
            if select:
                if self.current_selection:
                    self.current_selection.selected = False
                self.current_selection = new
            self.add_widget(new)

    def remove_filter(self, index=None):
        if not len(self.children) > 1:
            return

        if not index:
            rem = self.current_selection
            for i, x in enumerate(self.children):
                if x == self.current_selection:
                    if i > 0:
                        self.select_filter(self.children[i-1])
                    else:
                        self.select_filter(self.children[i+1])
                    break
            self.remove_widget(rem)

    def select_index(self, index):
        try:
            self.select_filter(self.children[-index])
        except Exception as e:
            print(e)

    def select_previous(self):
        for i, x in enumerate(self.children):
            if x.selected:
                if i == len(self.children) - 1:
                    self.select_filter(self.children[0])
                else:
                    self.select_filter(self.children[i+1])
                break

    def select_next(self):
        for i, x in enumerate(self.children):
            if x.selected:
                if i == 0:
                    self.select_filter(self.children[-1])
                else:
                    self.select_filter(self.children[i-1])
                break

    def select_filter(self, widget):
        if self.current_selection:
            self.current_selection.selected = False
        self.current_selection = widget
        widget.selected = True
        self.current_selection_text = widget.text


class FilterTab(Button):
    selected = BooleanProperty()
    index = None

    def __init__(self, **kwargs):
        super(FilterTab, self).__init__(**kwargs)

    def on_release(self):
        self.parent.select_filter(self)


Builder.load_string('''
<TabHolder>:
    width: self.minimum_width
    orientation: 'horizontal'
    viewclass: 'FilterTab'
    spacing: int(cm(0.1))

<FilterTab>:
    font_size: self.height * 0.5
    background_normal: 'images/blue_dark.png' if self.selected else 'images/blue_greyer.png'
    background_down: 'images/blue_bright.png'
''')
