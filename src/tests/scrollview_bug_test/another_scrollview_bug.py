from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App


class Root1(ScrollView):
    def init(self):
        self.add_widget(BoxLayout())
        for i in range(200):
            self.children[0].add_widget(
                Button(text=str(i), size_hint_y=None, height=50))
        self._viewport._trigger_layout.is_triggered = 22
        print(self._viewport._trigger_layout.is_triggered)


class Root2(RecycleView):
    def init(self):
        self.viewclass = 'Button'
        self.add_widget(RecycleBoxLayout())
        self.data = [{'text': i} for i in range(200)]
        # self._viewport._trigger_layout.is_triggered = 22
        if hasattr(self._viewport._trigger_layout, 'is_triggered'):
            print(self._viewport._trigger_layout.is_triggered)

class TestApp(App):
    def build(self):
        root = self.testwi()
        root.init()
        return root


app = TestApp()
# app.testwi = Root1
app.testwi = Root2
app.run()
