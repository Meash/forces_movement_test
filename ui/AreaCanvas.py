from tkinter import Canvas

__author__ = 'Martin'


class AreaCanvas(Canvas):
    def __init__(self, master, boundary, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(background='gray')

        ll = boundary.lower_left
        ur = boundary.upper_right

        self.create_line(ll.x, ll.y, ll.x, ur.y)
        self.create_line(ll.x, ur.y, ur.x, ur.y)
        self.create_line(ur.x, ll.y, ur.x, ur.y)
        self.create_line(ll.x, ll.y, ur.x, ll.y)
