from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App


current_instance = None


def get_context_box(pos):
    global current_instance
    app = App.get_running_app()
    if not current_instance or current_instance.dismissed:
        print('NN', pos)
        current_instance = ContextMenu(pos=pos)
        app.root.ids.floater.add_widget(current_instance)
        return current_instance
    return None


class ContextMenu(BoxLayout):
    dismissed = False

    def __init__(self, **kwargs):
        super(ContextMenu, self).__init__(**kwargs)
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.orientation = 'vertical'

    def open():
        dismissed = False
        print(1)

    def dismiss():
        print(2)
        dismissed = True
