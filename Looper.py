from threading import Timer

__author__ = 'Martin'


class Looper:
    def __init__(self, timeout, copters):
        self.timeout = timeout
        self.copters = copters
        self.timer = None

    def start(self):
        self.run_timer()

    def run_timer(self):
        self.timer = Timer(self.timeout, self.update)
        self.timer.name = "Looper Timer"
        self.timer.daemon = True
        self.timer.start()

    def update(self):
        for copter in self.copters:
            copter.update()

        self.run_timer()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
