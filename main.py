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

def set_up_robot(grid_size, name, identifer):
    """Set up the robot's initial position, direction, and associated details.

    Args:
        grid_size (int): The size of the grid.
        name (str): Name of the robot.
        identifier (int): Unique ID for the robot.

    Returns:
        robot (dict): A dictionary containing the robot's ID, name, position, and direction.
        directions (list): A list of possible directions the robot can face.
    """ 

    position = get_random_start(grid_size)
    direction, directions = get_random_direction()

    robot = {"id": identifer, "name": name, "position": position, "direction": direction}
    
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

def get_names_list(filename):
    """Load a list of robot names from a file and randomly select three.

    Args:
        filename (str): The name of the file containing robot names.

    Returns:
        names (list): A list of three randomly selected robot names.
    """
    all_names = []
    textfile = open(filename)
    for line in textfile:
        line = line.strip()
        all_names.append(line)

    names = random.sample(all_names,3)
    return names

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

def print_greeting(name, identifier, position , direction):
    """Print a greeting message that includes the robot's name, ID, position, and direction.

    Args:
        name (str): The robot's name.
        identifier (int): The robot's ID.
        position (tuple): The robot's current row and column coordinates.
        direction (str): The robot's current direction.
    """
    print_name_id(name, identifier)
    print_location_direction(position, direction)

    pass

def print_name_id(name, identifier):
    """ Print message with name and ID.

    Args:
        name (int): Name
        identifier (int): ID
    
    """
    print(f"Hello. My name is {name}. My ID is {identifier}.")
    pass

def print_location_direction(robot):
    """ Print message with location and direction.

    Args:
        robot (dict): A dictionary containing the robot's details, including position and direction.
    """
    print(f"My current location is {robot['position']}. I am facing {robot['direction']}.")
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
    

# Navigate to drink

def navigate(robot, directions, grid_size, target_position):
    """Navigate the robot towards its target position.

    The robot moves to the edge of the grid in its current direction, then rotates 90 degrees clockwise
    if it has not reached the target, and repeats the process until it reaches the target.

    Args:
        robot (dict): A dictionary containing the robot's details, including position and direction.
        directions (list): A list of possible directions the robot can face.
        grid_size (int): The size of the grid.
        target_position (tuple): The target row and column coordinates.
    """
    while not is_bot_at_target(robot, target_position): 

        robot = move_to_edge(robot, grid_size)

        if is_bot_at_target(robot, target_position):
            break

        robot = rotate(directions, robot)

    print(f"I am drinking milk, I am happy!")    
 
    pass

def is_bot_at_target(robot, target_position):
    """Check if the robot has reached its target position.

    Args:
        robot (dict): A dictionary containing the robot's details, including position.
        target_position (tuple): The target row and column coordinates.

    Returns:
        bool: True if the robot is at the target position, False otherwise.
    """
    
    return robot['position'][0] == target_position[0] and robot['position'][1] == target_position[1]

def is_bot_facing_wall(robot, grid_size):
    """Check if the robot is facing a wall (edge of the grid).

    Args:
        robot (dict): A dictionary containing the robot's details, including position and direction.
        grid_size (int): The size of the grid.

    Returns:
        facing_wall (bool): True if the robot is facing a wall, False otherwise.
    """

    row = robot['position'][0]
    col = robot['position'][1]
    direction = robot['direction']

    return (direction == 'North' and row == 0
           or direction == 'East' and col == (grid_size - 1)
           or direction == 'South' and row == (grid_size - 1)
           or direction == 'West' and col == 0)

        
def move_to_edge(robot, grid_size):
    """Move the robot in its current direction until it reaches the edge of the grid.

    Args:
        robot (dict): A dictionary containing the robot's details, including position and direction.
        grid_size (int): The size of the grid.

    Returns:
        robot (dict): The updated robot dictionary with its new position.
    """

    while not is_bot_facing_wall(robot, grid_size):
        print('Moving one step forward')
        robot = step(robot)
        print_location_direction(robot)
    
    return robot

def step(robot):
    """Move the robot one step in its current direction.

    Args:
        robot (dict): A dictionary containing the robot's details, including position and direction.

    Returns:
        robot (dict): The updated robot dictionary with its new position.
    """
    row = robot['position'][0]
    col = robot['position'][1]
    direction = robot['direction']
    
    if direction == 'North':
        row -= 1 
    elif direction == 'South':         
        row += 1 
    elif direction == 'East':        
        col += 1  
    elif direction == 'West':
        col -= 1
        
    robot['position'] = (row, col)
    
    return robot
    

def rotate(directions, robot):
    """Rotate the robot 90 degrees clockwise.

    Args:
        directions (list): A list of possible directions.
        robot (dict): A dictionary containing the robot's details, including direction.

    Returns:
        robot (dict): The updated robot dictionary with its new direction.
    """
    print('I have a wall in front of me')
    print('Turning 90 degrees clockwise')
    index = directions.index(robot['direction'])
    index = (index + 1) % 4
    robot['direction'] = directions[index]
    
    return robot
    

# Root function

def run_simulation(grid_size=10):
    """Start the robot navigation simulation.

    Print the name and ID for each robot, then navigate each robot towards its target position.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
    """
    # Get three random robot names and IDs. Means you cant pick same name twice.
    
    names, ids = print_group_names_ids()

    print()

    robots = []

    for i in range(len(names)):

        # Initialise robot position and direction. Store in dictionary.
        name = names[i]
        identifier = ids[i]
        robot, directions = set_up_robot(grid_size, name, identifier)
        robots.append(robot)
        target_position = get_targets(i)

        # Search for drink
        print(f"{name} is searching for its drink")
        print_location_direction(robot)
        navigate(robot, directions, grid_size, target_position)
        print()
    
    pass        

grid_size = 10    # Global variable      
run_simulation()










