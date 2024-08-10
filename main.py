from robot import Robot
import random

'''
1. Set up robot
    a. Get name
    b. Get identifier
    c. Get random starting position
    d. Get random starting direction
2. Print robot greeting
    a. Print name and identifier
    b. Print location and direction
3. Navigate to drink
    a. While not at (grid_size - 1, grid_size - 1).
        a. Move in direction to edge
            a. Move one step.
            b. Print location and direction after each step.
            c. Check if at edge.
            b. At edge, print 'at wall'
        d. Turn 90 degrees clockwise.
'''

# Set up robot

def set_up_robot(grid_size, all_names, prev_id, chosen_names):
    """Set up the robot's initial position, direction, and associated details.

    Args:
        grid_size (int): The size of the grid.
        name (str): Name of the robot.
        identifier (int): Unique ID for the robot.

    Returns:
        robot (dict): A dictionary containing the robot's ID, name, position, and direction.
        directions (list): A list of possible directions the robot can face.
    """ 

    name = generate_robot_name(all_names, chosen_names)
    identifier = generate_robot_id(prev_id)
    position = get_random_start(grid_size)
    direction, directions = get_random_direction()

    robot = Robot(identifier, name, position, direction)
    
    return robot, directions

def get_random_start(grid_size):
    """ Random allocation of starting position.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        position (tuple): A tuple representing the robot's row and column coordinates.
    """
    position = tuple(random.sample(range(grid_size - 1), 2))
    return position

def get_random_direction():
    """ Random allocation of starting direction.

        Also defines the possible directions as a list of strings

    Args:
        none

    Returns:
        direction (str): Direction string
        directions (list): List of possible directions
        
    """
    directions = ['North','East','South','West']
    direction = random.choice(directions)
    return direction, directions

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

def generate_robot_name(all_names, chosen_names):
    """ Select a robot's name at random from a given list

    Args:
        namelist (list): A list of candidate names. Will return "Robot" if not provided.
        
    Returns:
        str : Robot name
    """
    if len(all_names) > 0:
        name = random.choice(all_names)
        if name not in chosen_names:
            chosen_names.append(name)
            return name
        else:
            return generate_robot_name(all_names, chosen_names)
    else:
        return "Robot"

def generate_robot_id(prev_id):
    """ Generate a unique ID for the robot. 

    If prev_id is given and is >=0, the function will return prev_id+1
    Otherwise, the function will generate a random number between 1 to 1,000,000 as an ID.

    Returns:
        int : robot ID
    """
    if prev_id >= 0:
        return prev_id + 1
    else:
        return random.randint(1, 1000000)


def get_targets(i):
    """Get the target position for a robot based on its index.

    Args:
        i (int): The index of the robot.

    Returns:
        target_position (tuple): A tuple representing the target row and column coordinates.
    """
    targets = [(9,9),(9,0),(0,9)]
    target_position = targets[i]    
    return target_position

# Print robot greeting

def print_name_id(name, identifier):
    """ Print message with name and ID.

    Args:
        name (int): Name
        identifier (int): ID
    
    """
    print(f"Hello. My name is {name}. My ID is {identifier}.")
    pass


def print_group_names_ids():
    """Print the names and IDs of a group of robots.

    Returns:
        names (list): A list of robot names.
        ids (list): A list of robot IDs.
    """

    names = get_names_list('robot_names.txt')
    identifier = 1000
    ids = []

    for name in names:
        identifier += 1
        ids.append(identifier)
        print_name_id(name, identifier)
    return names, ids

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

    robots = []
    prev_id = 1000
    chosen_names =[]

    for i in range(n_of_robots):
        robot, directions = set_up_robot(grid_size, all_names, prev_id, chosen_names)
        robots.append(robot)
        prev_id = robot.id
        

    # Print greeting for each robot

    for robot in robots:
        print_name_id(robot.name, robot.id)
    
    print() # New line

    # Each robot navigate to drink

    for i in range(n_of_robots):

        print(f"{robots[i].name} is searching for its drink")
        robot.print_location_direction()
        target_position = get_targets(i)
        robot.navigate(directions, grid_size, target_position)
        print()
    
    pass        

grid_size = 10 # Global variable
n_of_robots = 3
run_simulation(grid_size, n_of_robots)


# target generation needs n_of_robots as input
# put greeting action into robot class









