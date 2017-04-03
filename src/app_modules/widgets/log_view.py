from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
# from kivy.uix.recycleview import RecycleView
from .recycleview import AppRecycleView
from kivy.uix.behaviors import FocusBehavior
from kivy.properties import BooleanProperty, NumericProperty
from kivy.core.clipboard import Clipboard
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.metrics import cm
from app_modules import key_binder
from kivy.clock import Clock


class LogViewClass(RecycleDataViewBehavior, Label):
    selected = BooleanProperty(False)
    index = None

    def __init__(self, **kwargs):
        super(LogViewClass, self).__init__(**kwargs)

    # def on_touch_down(self, touch):
    #     if self.collide_point(*touch.pos):
    #         Clipboard.copy(self.text0)

    def refresh_view_attrs(self, rv, index, data):
        super(LogViewClass, self).refresh_view_attrs(rv, index, data)
        self.index = index
        # print (self.selected)

    # def on_touch_down(self, touch):
    #     if self.collide_point(*touch.pos):
    #         pass
    def apply_selection(self, is_selected):
        self.selected = is_selected


class LogLayout(AppRecycleView):

    def __init__(self, **kwargs):
        super(LogLayout, self).__init__(**kwargs)

    def page_down(self):
        scroll = self.convert_distance_to_scroll(0, self.height)[1] * 0.9
        self.scroll_y = max(self.scroll_y - scroll, 0.0)

    def page_up(self):
        scroll = self.convert_distance_to_scroll(0, self.height)[1] * 0.9
        self.scroll_y = min(self.scroll_y + scroll, 1.0)

    def scroll_to_index(self, index, wheight):
        # self.scroll_y = (len(self.data) / wheight) * index
        print (len(self.data), wheight, index)
        print ('STI ', index)


class SelectableRecycleBoxLayout(RecycleBoxLayout):
    selected_widgets = None
    first_selection = -1

    def __init__(self, **kwargs):
        super(SelectableRecycleBoxLayout, self).__init__(**kwargs)
        key_binder.add('arrow_up', 273, 'down', self.on_arrow_up)
        key_binder.add('arrow_down', 274, 'down', self.on_arrow_down)
        self.selected_widgets = set()

    def get_modifier_mode(self):
        mode = ''
        if key_binder.ctrl_held and key_binder.shift_held:
            mode = ''
        elif key_binder.ctrl_held:
            mode = 'ctrl'
        elif key_binder.shift_held:
            mode = 'shift'
        return mode

    def on_arrow_up(self):
        mode = self.get_modifier_mode()
        if self.children:
            if self.first_selection == -1:
                self.first_selection = 0
                self.selected_widgets = {0}
            elif not mode:
                self.first_selection -= 1
                self.selected_widgets = {self.first_selection}
        self._update_selected()
        self._scroll_to_selected()

    def on_arrow_down(self):
        mode = self.get_modifier_mode()
        if self.children:
            if self.first_selection == -1:
                self.first_selection = 0
                self.selected_widgets = {0}
            elif not mode:
                self.first_selection += 1
                self.selected_widgets = {self.first_selection}
        self._update_selected()
        self._scroll_to_selected()

    def _scroll_to_selected(self):
        for x in self.children:
            if x.selected:
                self.parent.scroll_to(
                    x, padding=self.default_size[1] * 1.0, animate=False)

    def _update_selected(self):
        for x in self.children:
            if x.index in self.selected_widgets:
                x.apply_selection(True)
            else:
                x.apply_selection(False)
