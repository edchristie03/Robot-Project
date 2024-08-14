from robot import Robot
from robot_init import RobotFactory
import random

def get_name_candidates(filename):
    """Load a list of robot names from a file..

    Args:
        filename (str): The name of the file containing robot names.

    Returns:
        names (list): A list of possible robot names.
    """
    all_names = []
    with open(filename) as textfile:
        for line in textfile:
            line = line.strip()
            all_names.append(line)

    return all_names


def get_targets(i):
    """Get the target position for a robot based on its index.

    Args:
        i (int): The index of the robot.

    Returns:
        target_position (tuple): A tuple representing the target row and column coordinates.
    """
    targets = [(9,9),(9,0),(0,9),(0,0)]
    target_position = targets[i]    
    return target_position


# Root function

def run_simulation(grid_size=10, n_of_robots=3):
    """Start the robot navigation simulation.

    Print the name and ID for each robot, then navigate each robot towards its target position.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
    """

    # Get possible candidate names
    
    all_names = get_name_candidates('robot_names.txt')

    # Initialise robots

    robot_factory = RobotFactory(grid_size, all_names)
    robots = robot_factory.create_robots(n_of_robots)  

    # Print greeting for each robot

    for robot in robots:
        robot.print_name_id()
    
    print() # New line

    # Each robot navigate to drink

    for i in range(n_of_robots):

        print(f"{robots[i].name} is searching for its drink")
        robot.print_location_direction()
        target_position = get_targets(i)
        robot.navigate(grid_size, target_position)
        print()
    
    pass        

grid_size = 10 # Global variable
n_of_robots = 4
run_simulation(grid_size, n_of_robots)


# neaten the factory module. 

# change name of functions to make code more readable

# update docustrings 











