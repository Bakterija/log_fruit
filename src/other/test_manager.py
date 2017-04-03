from kivy.clock import Clock
from . import fake_data
from kivy.logger import Logger

APP = None
ROOT = None

def init(app, root):
    global APP, ROOT
    Logger.info('TestManager: init')
    APP, ROOT = app, root
    Clock.schedule_once(first_frame, 0)
    Clock.schedule_once(after2sec, 2)
    Clock.schedule_interval(every_sec, 0)

def first_frame(*args):
    Logger.info('TestManager: first_frame')
    for x in range(1):
        for data in fake_data.data:
            APP.log_full.append(data)

def after2sec(*args):
    Logger.info('TestManager: after2sec')

def every_sec(*args):
    pass
