
import random 

class Grid:

    def __init__(self, size):
        """Constructor for Grid.

        Args:
            size (int): The size of the grid (assumed square).
        """
        self.size = size

        # Initialise grid based on size argument
        # ._cells (the grid) is dictionary: {location: [drinks present at location]}

        self._cells = {(x, y): [] for x in range(self.size) for y in range(self.size)}
   
    def generate_random_position(self):
        """Generates a random position within the grid.

        Returns:
            tuple: A tuple (x, y) representing a random position in the grid.
        """
        return tuple(random.sample(range(self.size), 2))

    def generate_random_corner_position(self):
        """Generates a random corner position within the grid.

        The corners are at (0, 0), (0, size-1), (size-1, 0), (size-1, size-1).

        Returns:
            tuple: A tuple (x, y) representing a random corner position in the grid.
        """
        return tuple(random.choices([0, self.size-1], k=2))

    def add_drink(self, location, drink):
        """Adds a drink to the specified location in the grid.

        Args:
            location (tuple): A tuple (x, y) representing the location in the grid.
            drink (Drink): The drink object to add to the specified location.
        """
        self._cells[location].append(drink)
        pass

    def add_drink_at_random_corner(self, drink):
        """Adds a drink to a random corner location in the grid.

        Args:
            drink (Drink): The drink object to add to a random corner location.
        """
        location = self.generate_random_corner_position()
        self.add_drink(location, drink)
        pass

    def get_drinks_at_cell(self, location):
        """Retrieves the list of drinks at the specified location.

        Args:
            location (tuple): A tuple (x, y) representing the location in the grid.

        Returns:
            list: A list of drinks present at the specified location.
        """
        return self._cells[location]

    def get_owner_drink(self, robot_favourite, location):
        """Checks if the robot's favourite drink is at the specified location and returns it if so.

        Args:
            robot_favourite (str): The robot's favourite drink.
            location (tuple): A tuple (x, y) representing the location in the grid.

        Returns:
            str or None: The favourite drink if found at the location, otherwise None.
        """
        drinks = self.get_drinks_at_cell(location)
        if robot_favourite in drinks:
            return robot_favourite

        
            
        

    
