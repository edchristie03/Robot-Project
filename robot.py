
class Robot:
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction

    def print_name_id(self):
        """ Print message with name and ID.

        Args:
            name (int): Name
            identifier (int): ID
        
        """
        print(f"Hello. My name is {self.name}. My ID is {self.id}.")
        pass


    def step(self):
        """Move the robot one step in its current direction.

        Args:
            robot (dict): A dictionary containing the robot's details, including position and direction.

        Returns:
            robot (dict): The updated robot dictionary with its new position.
        """
        row = self.position[0]
        col = self.position[1]
        direction = self.direction
        
        if self.direction == 'North':
            row -= 1 
        elif self.direction == 'South':         
            row += 1 
        elif self.direction == 'East':        
            col += 1  
        elif self.direction == 'West':
            col -= 1
            
        self.position = (row, col)
        
        return 

    def rotate(self, directions):
        """Rotate the robot 90 degrees clockwise.

        Args:
            directions (list): A list of possible directions.
            robot (dict): A dictionary containing the robot's details, including direction.

        Returns:
            robot (dict): The updated robot dictionary with its new direction.
        """
        print('I have a wall in front of me')
        print('Turning 90 degrees clockwise')
        index = directions.index(self.direction)
        index = (index + 1) % 4
        self.direction = directions[index]
        
        return 

    def move_to_edge(self, grid_size):
        """Move the robot in its current direction until it reaches the edge of the grid.

        Args:
            robot (dict): A dictionary containing the robot's details, including position and direction.
            grid_size (int): The size of the grid.

        Returns:
            robot (dict): The updated robot dictionary with its new position.
        """

        while not self.is_bot_facing_wall(grid_size):
            print('Moving one step forward')
            self.step()
            self.print_location_direction()
        
        return 

    def navigate(self, directions, grid_size, target_position):
        """Navigate the robot towards its target position.

        The robot moves to the edge of the grid in its current direction, then rotates 90 degrees clockwise
        if it has not reached the target, and repeats the process until it reaches the target.

        Args:
            robot (dict): A dictionary containing the robot's details, including position and direction.
            directions (list): A list of possible directions the robot can face.
            grid_size (int): The size of the grid.
            target_position (tuple): The target row and column coordinates.
        """
        while not self.is_bot_at_target(target_position): 

            self.move_to_edge(grid_size)

            if self.is_bot_at_target(target_position):
                break

            self.rotate(directions)

        print(f"I am drinking milk, I am happy!")    
     
        pass

    

    def is_bot_facing_wall(self, grid_size):
        """Check if the robot is facing a wall (edge of the grid).

        Args:
            robot (dict): A dictionary containing the robot's details, including position and direction.
            grid_size (int): The size of the grid.

        Returns:
            facing_wall (bool): True if the robot is facing a wall, False otherwise.
        """

        row = self.position[0]
        col = self.position[1]
        direction = self.direction

        return (direction == 'North' and row == 0
               or direction == 'East' and col == (grid_size - 1)
               or direction == 'South' and row == (grid_size - 1)
               or direction == 'West' and col == 0)

    def is_bot_at_target(self, target_position):
        """Check if the robot has reached its target position.

        Args:
            robot (dict): A dictionary containing the robot's details, including position.
            target_position (tuple): The target row and column coordinates.

        Returns:
            bool: True if the robot is at the target position, False otherwise.
        """
        
        return self.position[0] == target_position[0] and self.position[1] == target_position[1]


    def print_location_direction(self):
        """ Print message with location and direction.

        Args:
            robot (dict): A dictionary containing the robot's details, including position and direction.
        """
        print(f"My current location is {self.position}. I am facing {self.direction}.")
        pass








        

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
    
