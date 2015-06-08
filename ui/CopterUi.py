from ui.CopterDrawer import CopterDrawer
from ui.ObstaclesDrawer import ObstaclesDrawer

__author__ = 'Martin'


class CopterUi:
    def __init__(self, canvas, copter):
        super().__init__()
        copter_drawer = CopterDrawer(canvas, copter)
        copter.add_change_listener(copter_drawer)
        obstacles_drawer = ObstaclesDrawer(canvas)
        copter.add_obstacle_listener(obstacles_drawer)
