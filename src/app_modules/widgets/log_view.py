from kivy.properties import BooleanProperty, NumericProperty, ListProperty
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from .app_recycleview.recycleview import AppRecycleView
from .app_recycleview.recyclebox import AppRecycleBox
from kivy.uix.behaviors import FocusBehavior
from kivy.core.clipboard import Clipboard
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.metrics import cm
from app_modules import key_binder
from kivy.clock import Clock
from app_modules import global_things as globhandler
from .behaviors import HoverBehavior
from kivy.animation import Animation
from time import time


class LogViewClass(HoverBehavior, RecycleDataViewBehavior, Label):
    selected = BooleanProperty(False)
    selected_last = BooleanProperty(False)
    default_height = NumericProperty()
    background_color = ListProperty([0.2, 0.2, 0.2])
    color_selected = ListProperty([0.25, 0.35, 0.6])
    color_hovering = ListProperty([0.2, 0.24, 0.35])
    color_default = ListProperty([0.2, 0.2, 0.2])
    index = None

    def __init__(self, **kwargs):
        super(LogViewClass, self).__init__(**kwargs)
        self.shorten = True
        self.shorten_from = 'right'

    def refresh_view_attrs(self, rv, index, data):
        super(LogViewClass, self).refresh_view_attrs(rv, index, data)
        self.index = index
        self.long_text = data['text']
        if self.selected_last:
            if not self.parent:
                self.selected_last = False
            elif index != self.parent.sel_last:
                self.selected_last = False

    def on_touch_down(self, touch):
        if globhandler.opened_popups:
            return False
        if self.collide_point(*touch.pos):
            if touch.button == 'left':
                self.left_click(touch)
            elif touch.button == 'right':
                self.right_click(touch)
            return True

    def left_click(self, touch):
        self.parent.select_with_touch(self.index)

    def right_click(self, touch):
        self.parent.select_with_touch(self.index)
        self.parent.open_context_menu(pos=self.to_window(*touch.pos))

    def apply_selection(self, is_selected):
        self.selected = is_selected

    def on_selected(self, _, value):
        if value:
            self.background_color = self.color_selected

        else:
            self.background_color = self.color_default

    def on_selected_last(self, _, value):
        if value:
            self.shorten = False
            self.max_lines = 0
            self.text = self.long_text
            if self.index == self.parent.sel_last:
                self.text_size = [self.width, None]
                self.texture_update()
                if self.texture_size[1] > self.default_height:
                    self.height = int(self.texture_size[1])
                else:
                    self.text_size[1] = self.default_height
        else:
            self.height = self.default_height
            self.text_size = self.size
            self.shorten = True
            self.texture_update()

    def on_enter(self):
        if not self.selected:
            self.background_color = self.color_hovering

    def on_leave(self):
        if not self.selected:
            self.background_color = self.color_default


class LogLayout(AppRecycleView):
    pass


class SelectableRecycleBoxLayout(AppRecycleBox):
    def context_menu_function(self, pos):
        globhandler.open_log_cmenu(pos)
