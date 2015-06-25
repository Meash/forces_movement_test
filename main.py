import copy

from Looper import Looper
from copter.Copter import Copter
from copter.CopterSwarm import CopterSwarm
from copter.behaviour.FleeFromEverythingBehaviour import FleeFromEverythingBehaviour
from copter.behaviour.MoveToTargetBehaviour import MoveToTargetBehaviour
from copter.behaviour.MoveToTargetFleeBehaviour import MoveToTargetFleeBehaviour
from copter.behaviour.RandomDirectionBehaviour import RandomDirectionBehaviour
from copter.positioning.Boundary import Boundary
from copter.sensors.SensorMock import SensorMock
from geometry.PointVector import PointVector
from ui.AreaCanvas import AreaCanvas
from ui.CopterUi import CopterUi
from ui.DrawingFrame import DrawingFrame

__author__ = 'Martin'


class Main:
    BOUNDARY_WIDTH = 800
    HEIGHT = 600

    SWARM_SIZE = 10

    SENSOR_RANGE = 50
    MAX_SPEED = 5

    def __init__(self):
        boundary_offset = 5
        boundary = Boundary(PointVector(boundary_offset, boundary_offset),
                            PointVector(self.BOUNDARY_WIDTH - boundary_offset, self.HEIGHT - boundary_offset))
        copters = self.__create_copters(self.SWARM_SIZE, boundary)
        copter_swarm = CopterSwarm(copters)
        self.looper = Looper(1 / 24, copters)

        self.root = None
        self.__init_ui(boundary, copters)

    def __create_copters(self, amount, boundary):
        acceleration = self.MAX_SPEED / 5
        # behaviour = FleeFromEverythingBehaviour(RandomDirectionBehaviour(acceleration, self.MAX_SPEED))
        targetPoint = PointVector(2 / 3 * self.BOUNDARY_WIDTH, 2 / 3 * self.HEIGHT)
        # behaviour = MoveToTargetBehaviour(targetPoint)
        behaviour = MoveToTargetFleeBehaviour(targetPoint)
        sensor = None
        copters = []

        copter_offset = 15
        center_x = (boundary.lower_left.x + boundary.upper_right.x) / 3 - (amount / 2) * copter_offset
        center_y = (boundary.lower_left.y + boundary.upper_right.y) / 3
        for i in range(amount):
            position = PointVector(center_x + i * copter_offset, center_y)
            copter = Copter(sensor, copy.deepcopy(behaviour), position, boundary, self.MAX_SPEED)
            copters.append(copter)
        # update sensors
        for i in range(amount):
            other_copters = copters[:i] + copters[i + 1:]
            sensor = SensorMock(self.SENSOR_RANGE, boundary, other_copters)
            copters[i].set_sensor(sensor)
        return copters

    @staticmethod
    def __create_copters_uis(canvas, copters):
        copters_uis = []
        for copter in copters:
            copter_ui = CopterUi(canvas, copter)
            copters_uis.append(copter_ui)
        return copters_uis

    def __init_ui(self, boundary, copters):
        self.root = DrawingFrame()
        self.root.wm_title("PuLiCopter - forces_movement_test")
        geometry_string = str(self.BOUNDARY_WIDTH) + "x" + str(self.HEIGHT)
        self.root.geometry(geometry_string)

        canvas = AreaCanvas(self.root, boundary,
                            width=self.BOUNDARY_WIDTH, height=self.HEIGHT)
        self.__create_copters_uis(canvas, copters)

        canvas.pack()

    def run(self):
        self.looper.start()
        self.root.mainloop()
        self.looper.stop()


if __name__ == '__main__':
    main = Main()
    main.run()
