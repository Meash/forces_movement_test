__author__ = 'Martin'


class Changeable:
    def __init__(self):
        self.change_listeners = []

    def add_change_listener(self, listener):
        self.change_listeners.append(listener)

    def on_change(self):
        for listener in self.change_listeners:
            listener.on_change()
