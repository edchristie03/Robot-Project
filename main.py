
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
3. Navigate to Ribena
    a. While not at (grid_size - 1, grid_size - 1).
        a. Move in direction to edge
            a. Move one step.
            b. Print location and direction after each step.
            b. At edge, print 'at wall'
        d. Turn 90 degrees clockwise.
'''

# Set up robot

def set_up_robot(grid_size):
    name = input('What is the name of the robot? ')
    identifier = 1000
    row, column = get_random_start(grid_size)
    direction = get_random_direction()
    return name, identifier, row, column, direction

def get_random_start(grid_size):
    """ Random allocation of starting position.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        row (int): Row coordinate
        column (int): Column coordinate
    """
    row = random.randint(0, (grid_size - 1))
    column = random.randint(0,(grid_size - 1))
    return row, column

def get_random_direction():
    """ Random allocation of starting direction.

    Args:
        none

    Returns:
        direction (str): Direction string
    """
    directions = ['North','East','South','West']
    direction_list = random.sample(directions,1)
    direction = direction_list[0]
    return direction

def run_simulation(grid_size=10, target_row=9, target_col=9):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_row (int): The target row coordinate. Defaults to 9.
        target_col (int): The target column coordinate. Defaults to 9.

    Return:
    
    """
    name, identifier, row, column, direction = set_up_robot(grid_size)
    print(name, identifier, row, column, direction)
    
    pass

        
grid_size = 10         
run_simulation(grid_size=grid_size, target_row=(grid_size - 1))
