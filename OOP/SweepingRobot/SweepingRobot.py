from __future__ import print_function
from solution import sweep_kernel


class BasicRobot(object):
    def __init__(self, room, initial_pos, initial_dir):
        self.room = room
        # 0 -> block
        # 1 -> cleaned
        # 2 -> unvisited
        self.x, self.y = initial_pos
        self._x, self._y = initial_dir

    def printer(self):
        for i in range(len(self.room)):
            for j in range(len(self.room[0])):
                print(self.room[i][j], end=' ')
            print(' ')

    def finish(self):
        for i in range(len(self.room)):
            for j in range(len(self.room[0])):
                if self.room[i][j] == 2:
                    return False
        return True

    def clean(self):
        self.room[self.x][self.y] = 1

    def move(self):
        if 0 <= self.x + self._x < len(self.room) and 0 <= self.y + self._y < len(self.room[0]) and self.room[self.x + self._x][self.y + self._y] != 0:
            self.x += self._x
            self.y += self._y
            return True
        else:
            return False

    def turn_left(self, k):
        dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        idx = dir_list.index((self._x, self._y))
        idx = (idx + k) % 4
        self._x, self._y = dir_list[idx]

    def turn_right(self, k):
        dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)][::-1]
        idx = dir_list.index((self._x, self._y))
        idx = (idx + k) % 4
        self._x, self._y = dir_list[idx]


class RobotController(object):
    def __init__(self, room, initial_pos, initial_dir):
        self.instance = BasicRobot(room, initial_pos, initial_dir)

    def move(self):
        '''
        move forward in current direction
        return false if cannot move
        '''
        return self.instance.move()

    def turn_left(self, k):
        '''
        turn left k*90 degree
        '''
        self.instance.turn_left(k)

    def turn_right(self, k):
        '''
        turn right k*90 degree
        '''
        self.instance.turn_right(k)

    def clean(self):
        '''
        clean current position
        '''
        self.instance.clean()


def sweep(room, init_pos, init_dir):
    robot = RobotController(room, init_pos, init_dir)
    sweep_kernel(robot)
    # robot.instance.printer()
    return robot.instance.finish()
