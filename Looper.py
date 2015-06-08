from threading import Timer

__author__ = 'Martin'


class Looper:
    def __init__(self, timeout, copters):
        self.timeout = timeout
        self.copters = copters
        self.run = True

    def start(self):
        self.run_timer()

    def run_timer(self):
        Timer(self.timeout, self.update).start()

    def update(self):
        if not self.run:
            return

        for copter in self.copters:
            copter.update()

        self.run_timer()

    def stop(self):
        self.run = False
