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

    # Initialise robots and get their favourite drinks

    robot_factory = RobotFactory(grid_size, all_names)
    robots, drinks = robot_factory.create_robots(n_of_robots)

    

    # Initialise the above favourite drinks

    drink_factory = DrinkFactory(drinks)
    drinks = drink_factory.create_drinks(n_of_robots)

    print(robots[0])
    print(robots[1])
    print(robots[2])
    #print(robots[3])
    print()
    
    print(drinks[0])
    print(drinks[1])
    print(drinks[2])
    #print(drinks[3])

    # Print greeting for each robot

    for robot in robots:
        robot.greet()
    print() # New line

    # Each robot navigate to drink
    
    for robot in robots:

        print(f"{robot.name} is searching for {robot.favourite_drink}.")
        
        robot.print_location_direction()

        for drink in drinks:
            if robot.favourite_drink == drink.name:
                robot.navigate(grid_size, drink.location, drink.name)
        print()
        
    
    pass        

grid_size = 10 # Global variable
n_of_robots = 3
run_simulation(grid_size, n_of_robots)


# change name of functions to make code more readable

# update docustrings 











