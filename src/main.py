#!/usr/bin/env python3
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('kivy', 'exit_on_escape', 0)
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from app_modules.worker import worker, wlock
from kivy.uix.boxlayout import BoxLayout
from app_modules import hotkeys_global
from kivy.utils import escape_markup
from kivy.clock import Clock
from time import time, sleep
from kivy.app import App
from app_modules import global_thing_handler as globhandler
from other import test_manager
from kivy.logger import Logger
import traceback

TESTING = True


class RootWidget(BoxLayout):
    def focus_iput(self, *args):
        self.ids.filter_input.focus = True
        self.ids.filter_input.select_all()
        self.ids.rv.scroll_y = 0.5


class LogFruitApp(App):
    highlight_color = StringProperty('#00BFFF')
    last_log_time = NumericProperty()
    filter_text = StringProperty()
    log_filtered_len = NumericProperty()
    log_filtered = ListProperty()
    log_full_len = NumericProperty()
    log_full_len2 = StringProperty()
    log_full = ListProperty()
    log_queued = []
    fps = NumericProperty()
    fps_log = list(range(10))
    _do_update_log = False

    def build(self):
        self.worker = worker
        self.root = RootWidget()
        self.bind(log_filtered=self.update_rv_data)
        Clock.schedule_interval(self.read_logs, 0.5)
        Clock.schedule_interval(self.update_fps, 0)
        Clock.schedule_once(self.worker.start, 0)
        hotkeys_global.init_hotkeys(self)
        self.root.ids.tab_holder.bind(
            current_selection_text=lambda o,v: self.set_filter_text(v))
        if TESTING:
            test_manager.init(self, self.root)
        return self.root

    def on_log_full(self, _, value):
        self._do_update_log = True

    def update_rv_data(self, _, value):
        self.root.ids.rv.set_data(value)

    def set_filter_text(self, value):
        self.filter_text = value
        self.refilter_logs()
        self.log_filtered_len = len(self.log_filtered)

    def refilter_logs(self):
        with wlock():
            filter_len = len(self.filter_text)
            new_logs = []
            for x in self.log_full:
                b = x['text0'].find(self.filter_text)
                if b != -1:
                    c = b + filter_len
                    start = escape_markup(x['text0'][:b])
                    end = escape_markup(x['text0'][c:])
                    mid = x['text0'][b:c].replace(
                        self.filter_text,
                        '[color=%s]%s[/color]' % (
                            self.highlight_color,
                            escape_markup(self.filter_text)))
                    text = ''.join((start, mid, end))
                    new_logs.append(
                        {'time': x['time'], 'text': text, 'text0': x['text0']})
            self.log_filtered = new_logs

    def read_logs(self, *args):
        new_log = self.worker.read_queue()

        if new_log or self._do_update_log:
            if self._do_update_log:
                self._do_update_log = False

            self.log_full = list(self.log_full) + new_log

            if self.root.ids.rv.scroll_y in (0.0, 1.0):
                self.refilter_logs()

        self.log_full_len = len(self.log_full)
        self.log_full_len2 = '%s/%s' % (
            len(self.worker.queue), self.worker.added_msg)
        self.log_filtered_len = len(self.log_filtered)

    def globhandler_instruction(self, instr):
        globhandler.do_stringinstruction(instr)

    def clear_logs(self):
        self.log_full = []
        self.log_filtered = []

    def save_logs(self, logs):
        text = ''
        for item in logs:
            text = ''.join((text, item['text']))
        with open('savelog.txt', 'w') as f:
            f.write(text)

    def update_fps(self, *args):
        new_time = time()
        alltime = time() - self.fps_log[0]
        del self.fps_log[0]
        self.fps_log.append(new_time)
        self.fps = int(1.0 / (alltime / len(self.fps_log)))

    def on_start(self):
        globhandler.init()

    def on_stop(self):
        self.stop_worker()

    def stop_worker(self):
        self.worker.stop()

if __name__ == '__main__':
    app = LogFruitApp()
    try:
        app.run()
    except:
        Logger.error('App: %s' % (traceback.format_exc()))
        if hasattr(worker, 'proc'):
            worker.stop()
