from kivy.clock import Clock
from . import fake_data
from kivy.logger import Logger
from time import time

APP = None
ROOT = None
RV = None

def init(app, root):
    global APP, ROOT, RV
    Logger.info('TestManager: init')
    APP, ROOT = app, root
    RV = root.ids.rv
    Clock.schedule_once(first_frame, 0)
    Clock.schedule_once(after2sec, 2)
    Clock.schedule_interval(every_sec, 1)

def first_frame(*args):
    Logger.info('TestManager: first_frame')
    for x in range(1):
        for data in fake_data.data:
            APP.log_full.append(data)

def after2sec(*args):
    Logger.info('TestManager: after2sec')

def every_sec(*args):
    if ROOT.ids.rv.scroll_y == 0.0:
        text = fake_data.get_random_text()
        APP.log_full.append({'time': time(), 'text': text, 'text0': text})
