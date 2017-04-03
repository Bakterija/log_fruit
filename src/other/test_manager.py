from kivy.clock import Clock
from . import fake_data
from kivy.logger import Logger


class TestManager(object):

    def init(self, app, root):
        Logger.info('TestManager: init')
        self.app, self.root = app, root
        Clock.schedule_once(self.first_frame, 0)
        Clock.schedule_once(self.after2sec, 2)
        Clock.schedule_interval(self.every_sec, 0)

    def first_frame(self, *args):
        Logger.info('TestManager: first_frame')
        for x in range(1):
            for data in fake_data.data:
                self.app.log_full.append(data)

    def after2sec(self, *args):
        Logger.info('TestManager: after2sec')

    def every_sec(self, *args):
        pass
