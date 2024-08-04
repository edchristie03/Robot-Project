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

def set_up_robot(grid_size):
    """ Set up details for the robot starting position and grid

    Args:
        grid_size (int): The size of the grid.
        target_row (int): The target row coordinate.
        target_col (int): The target column coordinate. 
        
    Returns:
        name (str): Name of robot.
        identifier (int): ID
        row (int): Row coordinate
        column (int): Column coordinate 
        direction (str): Direction string
        directions (list): List of possible directions
        drink (str): Favourite drink of the robot
        
    """ 
    
    position = get_random_start(grid_size)
    direction, directions = get_random_direction()
    return position, direction, directions

def get_random_start(grid_size):
    """ Random allocation of starting position.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        row (int): Row coordinate
        column (int): Column coordinate
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
    all_names = []
    textfile = open(filename)
    for line in textfile:
        line = line.strip()
        all_names.append(line)

    names = random.sample(all_names,3)
    return names

def get_targets(i):
    targets = [(9,9),(9,0),(0,9)]
    target_position = targets[i]    
    return target_position

# Print robot greeting

def print_greeting(name, identifier, position , direction):
    """ Print robot greeting.

    Args:
        name (int): Name
        identifier (int): ID
        row (int): Row coordinate
        column (int): Column coordinate
        direction (str): Direction string

    """
    print_name_id(name, identifier)
    print_location_direction(position, direction)
    # drink = input('What is their favourite drink? ')
    # print(f"There is a glass of {drink} at position ({target_row}, {target_col}).")
    # input('Ready? ')
    pass

def print_name_id(name, identifier):
    """ Print message with name and ID.

    Args:
        name (int): Name
        identifier (int): ID
    
    """
    print(f"Hello. My name is {name}. My ID is {identifier}.")
    pass

def print_location_direction(position, direction):
    """ Print message with location and direction.

    Args:
        row (int): Row coordinate
        column (int): Column coordinate
        direction (str): Direction string
    """
    print(f"My current location is ({position[0]}, {position[1]}). I am facing {direction}.")
    pass

# Navigate to drink

def navigate(position, direction, directions, grid_size, target_position):
    """ Navigate to the target. Move to edge. Rotate 90 clcokwise while not at target.

    Args:
        row (int): Row coordinate
        column (int): Column coordinate
        direction (str): Direction string
        directions (list): List of possible directions
        grid_size (int): Size of NxN grid
        target_row (int): The target row coordinate.
        target_col (int): The target column coordinate.
        drink (str): Favourite drink of the robot.
        
    """
    while position[0] != target_position[0] or position[1] != target_position[1]:
        position = move_to_edge(position, direction)

        if position[0] == target_position[0] and position[1] == target_position[1]:
            break

        direction = rotate(directions, direction)   

    print(f"I am drinking milk, I am happy!")    
 
    pass

def move_to_edge(position, direction):
    """ Move in starting direction to the edge of the grid.

    Args:
        row (int): Row coordinate
        column (int): Column coordinate
        direction (str): Direction string
        grid_size (int): GLOBAL variable for the grid size
        
    Return:
        row (int): Row coordinate
        column (int): Column coordinate
        
    """
    if direction == 'North':
        while position[0] != 0:
            position = step(position, direction)
    elif direction == 'South':
        while position[0] != (grid_size - 1):
            position = step(position, direction)      
    elif direction == 'East':
        while position[1] != (grid_size - 1):
            position = step(position, direction)
    elif direction == 'West':
        while position[1] != 0:
            position = step(position, direction)

    return position

def step(position, direction):
    """ Move in starting direction to the edge of the grid.

    Args:
        row (int): Row coordinate
        column (int): Column coordinate
        direction (str): Direction string
        
    Return:
        row (int): Row coordinate
        column (int): Column coordinate
        
    """
    if direction == 'North':
        print('Moving one step forward') 
        position = (position[0] - 1, position[1]) 
        print_location_direction(position, direction)
    elif direction == 'South':        
        print('Moving one step forward') 
        position = (position[0] + 1, position[1])
        print_location_direction(position, direction)
    elif direction == 'East':        
        print('Moving one step forward') 
        position = (position[0], position[1] + 1)
        print_location_direction(position, direction)    
    elif direction == 'West':
        print('Moving one step forward') 
        position = (position[0], position[1] - 1)
        print_location_direction(position, direction)
    
    return position
    

def rotate(directions, direction):
    """ Rotate 90 degrees clockwise.

    Args:
        directions (list): List of possible directions
        direction (str): Direction string
        
    Return:
        direction (str): Direction string
        
    """
    print('I have a wall in front of me')
    print('Turning 90 degrees clockwise')
    index = directions.index(direction)
    index = (index + 1) % 4
    direction = directions[index]
    
    return direction
    

# Root function

def run_simulation(grid_size=10):
    """ Start robot navigation simulation.

        Print name and ID for each robot. Then navigate for each robot.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_row (int): The target row coordinate. Defaults to 9.
        target_col (int): The target column coordinate. Defaults to 9.

    Return:
    
    """
    names = get_names_list('robot_names.txt')
    identifier = 1000

    for name in names:
        identifier += 1
        print_name_id(name, identifier)

    print()

    for i in range(len(names)):
        name = names[i]
        target_position = get_targets(i)
        print(f"{name} is searching for its drink")
        position, direction, directions = set_up_robot(grid_size)
        print_location_direction(position, direction)
        navigate(position, direction, directions, grid_size, target_position)
        print()
    
    pass

        

grid_size = 10    # Global variable      
run_simulation()
