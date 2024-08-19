
class Robot:
    def __init__(self, identifier, name, position, direction, favourite_drink, grid, directions=['North','East','South','West']):
        """Constructor for Robot.

        Args:
            identifier (int): Unique ID for the robot.
            name (str): Name of the robot.
            position (tuple): Starting position of the robot (row, col).
            direction (str): Starting direction of the robot.
            favourite_drink (str): The robot's favourite drink.
            grid (Grid): The grid where the robot navigates.
            directions (list): List of possible directions the robot can face (default is ['North', 'East', 'South', 'West']).
        """
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction
        self.favourite_drink = favourite_drink
        self.grid = grid
        self.directions = directions

    def greet(self):
        print(f"Hello. My name is {self.name}. My ID is {self.id}. My favourite drink is {self.favourite_drink}.")
        pass

    def step(self):
        """Moves the robot one step in its current direction.

        The robot's position will be updated based on the direction it is facing.

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

    def rotate(self):
        """Rotates the robot 90 degrees clockwise, updating its direction.
        """
        print('I have a wall in front of me')
        print('Turning 90 degrees clockwise')
        index = self.directions.index(self.direction)
        index = (index + 1) % 4
        self.direction = self.directions[index]
        
        return 

    def move_to_edge(self):
        """Moves the robot in its current direction until it reaches the edge of the grid.

        The robot will continuously move forward until it encounters a wall (edge of the grid).

        """
        while not self.is_bot_facing_wall():
            print('Moving one step forward')
            self.step()
            self.print_location_direction()
        
        return 

    def get_drink(self):
        """Gets the robot's favourite drink at its current position, if available.

        Returns:
            drink (Drink or None): The drink at the robot's current position, or None if not found.
        """
        return self.grid.get_owner_drink(self.favourite_drink, self.position)

    def navigate(self):
        """Navigates the robot towards its favourite drink by moving to the edge and rotating.

        The robot moves to the edge of the grid in its current direction, rotates 90 degrees, 
        and repeats the process until it finds its favourite drink.

        Args:
            None
        """
        
        drink = self.get_drink()
        
        while drink is None:

            self.move_to_edge()
            drink = self.get_drink()

            if drink is not None:
                break

            self.rotate()
        
        print(f"I am drinking {self.favourite_drink}, I am happy!")    
     
        pass

    def is_bot_facing_wall(self):
        """Checks if the robot is facing a wall (the edge of the grid).

        Returns:
            facing_wall (bool): True if the robot is facing a wall, False otherwise.
        """
        row = self.position[0]
        col = self.position[1]
        direction = self.direction

        return (direction == 'North' and row == 0
               or direction == 'East' and col == (self.grid.size - 1)
               or direction == 'South' and row == (self.grid.size - 1)
               or direction == 'West' and col == 0)

    def print_location_direction(self):
        """ Print message with location and direction.
        """
        print(f"My current location is {self.position}. I am facing {self.direction}.")
        pass

    def __str__(self):
        return f"Robot called {self.name} with ID: {self.id}."








        

def _test_robot_init():
    name = "Bender"
    identifier = 1000
    position = (3, 5)
    direction = "n"
    
    robot = Robot(identifier, name, position, direction, favourite_drink, grid)
    assert isinstance(robot, Robot)
    assert robot.id == identifier
    assert robot.name == name
    assert robot.position == position
    assert robot.direction == direction
    
    
if __name__ == "__main__":
    _test_robot_init()


