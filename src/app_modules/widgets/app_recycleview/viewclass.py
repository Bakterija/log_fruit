class AppRecycleViewClass(object):
    selected = BooleanProperty(False)
    background_color = ListProperty([0.2, 0.2, 0.2])
    color_selected = ListProperty([0.25, 0.35, 0.6])
    color_hovering = ListProperty([0.2, 0.24, 0.35])
    color_default = ListProperty([0.2, 0.2, 0.2])
    index = None
