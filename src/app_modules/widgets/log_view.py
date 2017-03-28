from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.clipboard import Clipboard
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.metrics import cm


class LogViewClass(RecycleDataViewBehavior, Label):

    def __init__(self, **kwargs):
        super(LogViewClass, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            Clipboard.copy(self.text0)

    def refresh_view_attrs(self, rv, index, data):
        for k, v in data.items():
            setattr(self, k, v)


# class LogLayout(RecycleView):
#
#     def __init__(self, **kwargs):
#         super(LogLayout, self).__init__(**kwargs)
#         self.viewclass = 'LogView'
#
#         rbox = RecycleBoxLayout()
#         rbox.orientation = 'vertical'
#         rbox.size_hint = (1, None)
#         rbox.default_size = (None, int(cm(0.9)))
#         rbox.default_size_hint = (1, None)
#         rbox.spacing = int(cm(0.05))
#
#         rbox.bind(minimum_height=rbox.setter('height'))
#         self.add_widget(rbox)
