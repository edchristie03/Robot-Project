import random
from robot import Robot
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
    position = tuple(random.sample(range(grid_size), 2))
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
