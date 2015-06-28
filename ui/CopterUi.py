from ui.CopterDrawer import CopterDrawer
from ui.ObstaclesDrawer import ObstaclesDrawer
from ui.OtherCoptersDrawer import OtherCoptersDrawer

__author__ = 'Martin'


class CopterUi:
    def __init__(self, canvas, copter):
        super().__init__()
        copter_drawer = CopterDrawer(canvas, copter)
        copter.add_change_listener(copter_drawer)
        obstacles_drawer = ObstaclesDrawer(copter, canvas)
        copter.add_obstacle_listener(obstacles_drawer)
        other_copters_drawer = OtherCoptersDrawer(copter, canvas)
        copter.add_other_copters_listener(other_copters_drawer)
