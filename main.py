from robot import Robot
from robot_factory import RobotFactory
from drink import Drink
from drink_factory import DrinkFactory
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

    # Initialise drinks

    drink_factory = DrinkFactory(prev_id=1000)
    drinks = drink_factory.create_drinks(n_of_robots)

    # Print greeting for each robot

    for robot in robots:
        robot.greet()
    print() # New line

    # Each robot navigate to drink
    i = 0
    for robot in robots:

        print(f"{robot.name} is searching for {robot.favourite_drink}.")
        
        robot.print_location_direction()
        
        robot.navigate(grid_size, drinks[i].location, robot.favourite_drink)
        print()
        i += 1
    
    pass        

grid_size = 10 # Global variable
n_of_robots = 4
run_simulation(grid_size, n_of_robots)


# change name of functions to make code more readable

# update docustrings 











