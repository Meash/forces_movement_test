from tkinter import Canvas

__author__ = 'Martin'


class AreaCanvas(Canvas):
    def __init__(self, master, obstacles, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(background='gray')

        obstacle_entities = list(map(lambda obstacle: obstacle.geometric_entity, obstacles))
        for obstacle_entity in obstacle_entities:
            ll = obstacle_entity.lower_left
            ur = obstacle_entity.upper_right

            self.create_line(ll.x, ll.y, ll.x, ur.y)
            self.create_line(ll.x, ur.y, ur.x, ur.y)
            self.create_line(ur.x, ll.y, ur.x, ur.y)
            self.create_line(ll.x, ll.y, ur.x, ll.y)
