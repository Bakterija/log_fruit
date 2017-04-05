from kivy.app import App
from . import key_binder
from kivy.clock import Clock, mainthread

opened_popups = False

def init():
    global ROOT, LOG_CONTEXT_MENU
    APP = App.get_running_app()
    ROOT = APP.root
    LOG_VIEW = ROOT.ids.rv
    LOG_BOX = ROOT.ids.rv
    LOG_CONTEXT_MENU = ROOT.ids.context_menu0
    LOG_CONTEXT_MENU.bind(visible=on_cmenu_visible)

def open_log_cmenu(pos):
    LOG_CONTEXT_MENU.show(*pos)

def on_cmenu_visible(_, value):
    global opened_popups
    if value:
        key_binder.stop()
        opened_popups = True
    else:
        key_binder.start()
        Clock.schedule_once(set_opened_popups_false, 0.2)

def set_opened_popups_false(dt):
    global opened_popups
    opened_popups = False

def do_stringinstruction(instr):
    if instr['method'] == 'context_menu0_task':
        text = instr['text']
        if text == 'Edit':
            print('ED')
        elif text == 'Copy':
            print('Copy')
