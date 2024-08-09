class Robot:
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction

def _test_robot_init():
    name = "Bender"
    identifier = 1000
    position = (3, 5)
    direction = "n"
    
    robot = Robot(identifier, name, position, direction)
    assert isinstance(robot, Robot)
    assert robot.id == identifier
    assert robot.name == name
    assert robot.position == position
    assert robot.direction == direction
    
    
if __name__ == "__main__":
    _test_robot_init()
    
