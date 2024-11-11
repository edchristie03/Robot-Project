
from robot_factory import RobotFactory
from grid import Grid

def get_name_candidates(filename):
    """Load a list of robot names from a file.

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

    This function sets up a grid containing drinks, creates robots with random
    positions and favourite drinks,and makes each robot navigate to find its
    drink on the grid.

    Args:
        grid_size (int): The size of the grid (default is 10).
        n_of_robots (int): The number of robots to create and simulate (default is 3).
    """

    # Get possible candidate names
    
    all_names = get_name_candidates('robot_names.txt')

    # Create grid instance

    grid = Grid(grid_size)

    # Create and place drinks on the grid
    
    grid.create_and_place_drinks(n_of_robots)

    # Create robots whose favourite drinks are already on the grid  

    robot_factory = RobotFactory(grid, all_names)
    robots = robot_factory.create_robots(n_of_robots)

    # Print grid visualisation
    
    print(grid._cells)
        
    # Print greeting for each robot

    for robot in robots:
        robot.greet()
    print() 

    # Each robot navigate to drink
    
    for robot in robots:
        print(f"{robot.name} is searching for {robot.favourite_drink}.")
        robot.print_location_direction()
        robot.navigate()
        print()
        
    pass
    
grid_size = 10 # Global variable
n_of_robots = 3
run_simulation(grid_size, n_of_robots)













