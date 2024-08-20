import random
from robot import Robot


# Set up robot

class RobotFactory:
    
    def __init__(self, grid, all_names, chosen_names=[], prev_id=1000):
        """Constructor for RobotFactory.

        Args:
            grid (Grid): The grid where robots will navigate.
            all_names (list): A list of all possible robot names.
            chosen_names (list): A list of robot names already chosen (default is empty).
            prev_id (int): The previous robot ID, used to increment and assign unique IDs (default is 1000).
        """
        self.grid = grid
        self.all_names = all_names
        self.chosen_names = chosen_names
        self.prev_id = prev_id

    def create_robots(self, n_of_robots):
        """Creates a list of robots and their associated drinks.

        Args:
            n_of_robots (int): The number of robots to create.

        Returns:
            robots (list): A list of Robot objects.
            drinks (list): A list of drinks associated with each robot.
        """
        robots = []
        drinks_on_grid = self.grid.drinks

        for i in range(n_of_robots):
            drink = drinks_on_grid[i]
            robot = self.set_up_robot(drink)
            robots.append(robot)

        return robots

    # need to get name based on the drink using the dictionary

    def set_up_robot(self, drink):
        """Sets up the robot's initial attributes including name, ID, position, direction, and favourite drink.

        Returns:
            robot (Robot): A Robot object with the initialized attributes.
        """ 
        name = self.get_name_from_drink(drink)
        identifier = self.generate_robot_id()
        position = self.get_random_start()
        direction = self.get_random_direction()
        drink = drink.name

        robot = Robot(identifier, name, position, direction, drink, self.grid)
        
        return robot

    def get_random_start(self):
        """Random allocation of starting position.

        Returns:
            position (tuple): A tuple representing the robot's row and column coordinates on the grid.
        """  
        return self.grid.generate_random_position()

    def get_random_direction(self):
        """Randomly selects a starting direction for the robot.

        Returns:
            direction (str): The randomly selected direction ('North', 'East', 'South', 'West').
        """  
        return random.choice(['North','East','South','West'])

    def generate_robot_id(self):
        """Generates a unique ID for each robot, incrementing from the previous ID.

        Returns:
            identifier (int): A unique robot ID.
        """
        if self.prev_id >= 0:
            self.prev_id += 1
            return self.prev_id
        else:
            return random.randint(1, 1000000)

    def get_name_from_drink(self, drink):
        names = {'Cider': 'Ed', 'Maracuya': 'Yosh', 'Coffee': 'Sophie', 'Milk': 'Hester', 'Cerveza': 'Ramon'}
        return names[drink.name]
        

    def generate_robot_name(self):
        """Selects a unique robot name from the list of available names.

        Returns:
            name (str): The selected robot name.
        """
        if len(self.all_names) > 0:
            name = random.choice(self.all_names)
            if name not in self.chosen_names:
                self.chosen_names.append(name)
                return name
            else:
                return self.generate_robot_name()
        else:
            return "Robot"

    def get_favourite_drink(self, name):
        """Retrieves the favourite drink for a robot based on its name.

        Args:
            name (str): The robot's name.

        Returns:
            drink (str): The favourite drink of the robot.
        """
        drinks = {'Ed': 'Cider', 'Yosh': 'Maracuya', 'Sophie': 'Coffee', 'Hester': 'Milk', 'Ramon': 'Cerveza'}
        return drinks[name]
        
