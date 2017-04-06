# from scrollv import ScrollView
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock


class Root(ScrollView):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)

    def after_init(self):
        grid = GridLayout(cols=1, size_hint_y=None)
        grid.bind(minimum_height=lambda w,v: setattr(grid, 'height', v))
        self.add_widget(grid)
        for i in range(200):
            new = Button(text=str(i), size_hint_y=None, height=100)
            grid.add_widget(new)

class Test(App):
    def build(self):
        root = Root()
        root.after_init()
        Clock.schedule_once(lambda *a: setattr(root, 'scroll_y', 0.5), 0)
        return root


app = Test()
app.run()
