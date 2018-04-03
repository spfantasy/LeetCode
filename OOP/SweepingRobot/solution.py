# class RobotController(object):
#     def __init__(self, room, initial_pos, initial_dir):
#         self.instance = BasicRobot(room, initial_pos, initial_dir)

#     def move(self):
#         '''
#         move forward in current direction
#         return false if cannot move
#         '''

#     def turn_left(self, k):
#         '''
#         turn left k*90 degree
#         '''

#     def turn_right(self, k):
#         '''
#         turn right k*90 degree
#         '''

#     def clean(self):
#         '''
#         clean current position
#         '''


def sweep_kernel(robot):
    ###
    def clean(robot, coordinate, direction, record):
        dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        record.add(coordinate)
        robot.clean()
        curr_direction_idx = dir_list.index(direction)
        for i in range(4):
            if (coordinate[0] + direction[0], coordinate[1] + direction[1]) not in record:
                success = robot.move()
                if success:
                    new_coord = (
                        coordinate[0] + direction[0], coordinate[1] + direction[1])
                    clean(robot, new_coord, direction, record)
                    robot.turn_right(2)
                    robot.move()
                    robot.turn_right(2)
            robot.turn_right(1)
            curr_direction_idx = (curr_direction_idx + 1) % 4
            direction = dir_list[curr_direction_idx]
    clean(robot, (0, 0), (0, 1), set())
