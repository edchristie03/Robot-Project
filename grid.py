
import random 

class Grid:

    def __init__(self, size):
        self.size = size

        # Initialise grid based on size argument
        # ._cells (the grid) is dictionary: {location: [drinks present at location]}

        self._cells = {(x, y): [] for x in range(self.size) for y in range(self.size)}
   
    def generate_random_position(self):
        
        return tuple(random.sample(range(self.size), 2))

    def generate_random_corner_position(self):

        return tuple(random.choices([0, self.size-1], k=2))

    def add_drink(self):

    def add_drink_at_random_corner(self):

    def get_drinks_at_cell(self):

    def check_if_owner_drink(self):

    
