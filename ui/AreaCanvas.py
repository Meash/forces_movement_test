from tkinter import Canvas
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class AreaCanvas(Canvas):
    def __init__(self, master, obstacles, target_point, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(background='lightgray')

        height = kwargs['height']
        invert_y = lambda y: height - y

        target_cross_size = 5

        target_x = target_point.x
        target_y = invert_y(target_point.y)
        self.create_line(target_x - target_cross_size, target_y - target_cross_size,
                         target_x + target_cross_size, target_y + target_cross_size)
        self.create_line(target_x - target_cross_size, target_y + target_cross_size,
                         target_x + target_cross_size, target_y - target_cross_size)

        obstacle_entities = list(map(lambda obstacle: obstacle.geometric_entity, obstacles))
        for obstacle_entity in obstacle_entities:
            ll = obstacle_entity.lower_left
            ur = obstacle_entity.upper_right

            self.create_line(ll.x, invert_y(ll.y), ll.x, invert_y(ur.y))
            self.create_line(ll.x, invert_y(ur.y), ur.x, invert_y(ur.y))
            self.create_line(ur.x, invert_y(ll.y), ur.x, invert_y(ur.y))
            self.create_line(ll.x, invert_y(ll.y), ur.x, invert_y(ll.y))
