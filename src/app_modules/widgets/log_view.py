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


class LogViewClass(HoverBehavior, RecycleDataViewBehavior, Label):
    selected = BooleanProperty(False)
    background_color = ListProperty([0.2, 0.2, 0.2])
    color_selected = ListProperty([0.25, 0.35, 0.6])
    color_hovering = ListProperty([0.2, 0.24, 0.35])
    color_default = ListProperty([0.2, 0.2, 0.2])
    index = None

    def __init__(self, **kwargs):
        super(LogViewClass, self).__init__(**kwargs)

    def refresh_view_attrs(self, rv, index, data):
        super(LogViewClass, self).refresh_view_attrs(rv, index, data)
        self.index = index

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

    def on_enter(self):
        if not self.selected:
            self.background_color = self.color_hovering

    def on_leave(self):
        self.on_selected(None, self.selected)


class LogLayout(AppRecycleView):
    pass


class SelectableRecycleBoxLayout(AppRecycleBox):
    def context_menu_function(self, pos):
        globhandler.open_log_cmenu(pos)
