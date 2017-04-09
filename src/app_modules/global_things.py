from app_modules.widgets.text_editor import TextEditorPopup
from kivy.clock import Clock, mainthread
from kivy.core.clipboard import Clipboard
from kivy.app import App
from . import key_binder

opened_popups = set()

def init():
    APP = App.get_running_app()
    ROOT = APP.root
    LOG_VIEW = ROOT.ids.rv
    LOG_BOX = ROOT.ids.rv.children[0]
    LOG_CONTEXT_MENU = ROOT.ids.context_menu0
    LOG_CONTEXT_MENU.bind(visible=on_cmenu_visible)
    globals().update(locals())

def open_log_cmenu(pos):
    LOG_CONTEXT_MENU.show(*pos)

def on_cmenu_visible(_, value):
    if value:
        opened_popup_add('context_menu0')
    else:
        Clock.schedule_once(rem_opened_ctx_menu0, 0.2)

def rem_opened_ctx_menu0(dt):
    opened_popup_remove('context_menu0')

def opened_popup_add(name):
    opened_popups.add(name)
    on_opened_popups(opened_popups)

def opened_popup_remove(name):
    opened_popups.remove(name)
    on_opened_popups(opened_popups)

def on_opened_popups(value):
    if value:
        key_binder.stop_categories('n/a')
    else:
        key_binder.start_categories('n/a')

def do_stringinstruction(instr):
    if instr['method'] == 'context_menu0_task':
        text = instr['text']
        if text == 'Edit':
            # selected = LOG_BOX.get_widget_from_index(LOG_BOX.selected_widgets)
            text = ''
            for x in LOG_BOX.selected_widgets:
                text = ''.join((text, LOG_VIEW.data[x]['text0'], '\n'))
            popup_id = 'text_editor'
            on_dismiss = lambda a: opened_popup_remove(popup_id)
            text_editor = TextEditorPopup(
                on_dismiss=on_dismiss, text=text)
            text_editor.open()
            opened_popup_add(popup_id)
        elif text == 'Copy':
            widget = LOG_BOX.get_widget_from_index(LOG_BOX.sel_last)
            Clipboard.copy(widget.text0)
        LOG_CONTEXT_MENU.hide()

def kb_enter():
    if LOG_CONTEXT_MENU.visible:
        LOG_CONTEXT_MENU.select_hovered()

def kb_arrow_up():
    if LOG_CONTEXT_MENU.visible:
        LOG_CONTEXT_MENU.arrow_up()

def kb_arrow_down():
    if LOG_CONTEXT_MENU.visible:
        LOG_CONTEXT_MENU.arrow_down()

def kb_escape():
    if opened_popups:
        if LOG_CONTEXT_MENU.visible:
            LOG_CONTEXT_MENU.hide()
    else:
        APP.stop()
