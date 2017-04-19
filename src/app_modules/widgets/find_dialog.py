from kivy.uix.behaviors import DragBehavior
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock


class FindDialog(ModalView):
    def __init__(self, **kwargs):
        super(FindDialog, self).__init__(**kwargs)
        self.size_hint = (0.7, 0.2)
        self.center = (Window.system_size[0] * 0.5 , Window.system_size[1] * 0.5)
        # self.size = (1, 1)
        self.background_color = (0, 0, 0, 0)
        self.source = ''
        self.auto_dismiss = False
        self.add_widget(FindDialogWidget())
        self.pos = (-200, 300)

    def open(self, *largs):
        self._window = self._search_window()
        if not self._window:
            Logger.warning('ModalView: cannot open view, no window found.')
            return
        self._window.add_widget(self)


class FindDialogWidget(DragBehavior, Label):
    def __init__(self, **kwargs):
        super(FindDialogWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)


Builder.load_string('''
<FindDialogWidget>:
    canvas.before:
        Color:
            rgba: 0.4, 0.4, 0.2, 1
        Rectangle:
            pos: self.pos
            size: self.size
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0
''')
