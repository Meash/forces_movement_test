import copy

from Looper import Looper
from copter.Copter import Copter
from copter.CopterSwarm import CopterSwarm
from copter.behaviour.MoveToTargetFleeBehaviour import MoveToTargetFleeBehaviour
from copter.environment.Obstacle import Obstacle
from copter.positioning.Boundary import Boundary
from copter.sensors.SensorMock import SensorMock
from geometry.PointVector import PointVector
from geometry.Rectangle import Rectangle
from ui.AreaCanvas import AreaCanvas
from ui.CopterUi import CopterUi
from ui.DrawingFrame import DrawingFrame

__author__ = 'Martin'


class Main:
    BOUNDARY_OFFSET = 5
    BOUNDARY_WIDTH = 800
    HEIGHT = 600

    SWARM_SIZE = 10

    SENSOR_RANGE = 50
    MAX_SPEED = 5

    def __init__(self):
        boundary = Boundary(PointVector(self.BOUNDARY_OFFSET, self.BOUNDARY_OFFSET),
                            PointVector(self.BOUNDARY_WIDTH - self.BOUNDARY_OFFSET, self.HEIGHT - self.BOUNDARY_OFFSET))
        start_pos = PointVector((boundary.lower_left.x + boundary.upper_right.x) / 3,
                                (boundary.lower_left.y + boundary.upper_right.y) / 3)
        obstacles = self.get_boundary_lines(boundary)

        copters = self.__create_copters(self.SWARM_SIZE, start_pos, obstacles)
        copter_swarm = CopterSwarm(copters)
        self.looper = Looper(1 / 24, copters)

        self.root = None
        self.__init_ui(obstacles, copters)

    def __create_copters(self, amount, start_pos, obstacles):
        acceleration = self.MAX_SPEED / 5
        # behaviour = FleeFromEverythingBehaviour(RandomDirectionBehaviour(acceleration, self.MAX_SPEED))
        targetPoint = PointVector(2 / 3 * self.BOUNDARY_WIDTH, 2 / 3 * self.HEIGHT)
        # behaviour = MoveToTargetBehaviour(targetPoint)
        behaviour = MoveToTargetFleeBehaviour(targetPoint)
        sensor = None
        copters = []

        copter_offset = 15
        center_x = start_pos.x - (amount / 2) * copter_offset
        center_y = start_pos.y
        for i in range(amount):
            position = PointVector(center_x + i * copter_offset, center_y)
            copter = Copter(sensor, copy.deepcopy(behaviour), position, self.MAX_SPEED)
            copters.append(copter)
        # update sensors
        for i in range(amount):
            other_copters = copters[:i] + copters[i + 1:]
            sensor = SensorMock(self.SENSOR_RANGE, obstacles, other_copters)
            copters[i].set_sensor(sensor)
        return copters

    @staticmethod
    def get_boundary_lines(boundary):
        ll = boundary.lower_left
        ul = boundary.upper_left
        ur = boundary.upper_right
        lr = boundary.lower_right
        boundary_lines = [Obstacle(Rectangle(PointVector(ll.x, ll.y),
                                             PointVector(ul.x, ul.y))),
                          Obstacle(Rectangle(PointVector(ul.x, ul.y),
                                             PointVector(ur.x, ur.y))),
                          Obstacle(Rectangle(PointVector(ur.x, ur.y),
                                             PointVector(lr.x, lr.y))),
                          Obstacle(Rectangle(PointVector(lr.x, lr.y),
                                             PointVector(ll.x, ll.y)))]
        return boundary_lines

    @staticmethod
    def __create_copters_uis(canvas, copters):
        copters_uis = []
        for copter in copters:
            copter_ui = CopterUi(canvas, copter)
            copters_uis.append(copter_ui)
        return copters_uis

    def __init_ui(self, obstacles, copters):
        self.root = DrawingFrame()
        self.root.wm_title("PuLiCopter - forces_movement_test")
        geometry_string = str(self.BOUNDARY_WIDTH) + "x" + str(self.HEIGHT)
        self.root.geometry(geometry_string)

        canvas = AreaCanvas(self.root, obstacles,
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
