from . import key_binder


def init_hotkeys(self):
    key_binder.log_keys = True
    ids = self.root.ids

    key_binder.add(
        'focus_input', 108, 'down',
        self.root.focus_iput, modifier=['ctrl'])

    key_binder.add(
        'tab_add', 116, 'down',
        self.root.ids.tab_holder.add_filter, modifier=['ctrl'])

    key_binder.add(
        'tab_remove', 119, 'down',
        self.root.ids.tab_holder.remove_filter, modifier=['ctrl'])

    def page_up_or_prev_tab():
        if key_binder.ctrl_held:
            self.root.ids.tab_holder.select_previous()
        else:
            self.root.ids.rv.page_up()

    def page_down_or_next_tab():
        if key_binder.ctrl_held:
            self.root.ids.tab_holder.select_next()
        else:
            self.root.ids.rv.page_down()

    key_binder.add('page_tab_prev', 280, 'down', page_up_or_prev_tab)
    key_binder.add('page_tab_next', 281, 'down', page_down_or_next_tab)

    key_binder.add(
        'scroll_home', 278, 'down',
        lambda *a: setattr(self.root.ids.rv, 'scroll_y', 1.0))
    key_binder.add(
        'scroll_end', 279, 'down',
        lambda *a: setattr(self.root.ids.rv, 'scroll_y', 0.0))

    for i in range(10):
        key_binder.add(
            'sel_tab_%s' % (i), 48+i, 'down',
            lambda i=i: self.root.ids.tab_holder.select_index(i),
            modifier=['alt']
        )
