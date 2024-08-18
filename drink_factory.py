
import random
from drink import Drink


class DrinkFactory:

    def __init__(self, all_names, chosen_names=[]):
        self.all_names = all_names
        self.chosen_names = chosen_names
        pass

        
    def create_drinks(self, n_of_robots):
        drinks = []

        for i in range(n_of_robots):
            drink = self.set_up_drink()
            drinks.append(drink)

        return drinks

    def set_up_drink(self):

        
        name = self.get_drink_name()
        
        location = self.get_drink_location()

        drink = Drink(name, location)

        return drink

        
    '''
    def generate_drink_id(self, name):
        """ Generate a unique ID for the robot. 

        If prev_id is given and is >=0, the function will return prev_id+1
        Otherwise, the function will generate a random number between 1 to 1,000,000 as an ID.

        Returns:
            int : robot ID
        """
        if self.prev_id >= 0:
            self.prev_id += 1
            return self.prev_id
        else:
            return random.randint(1, 1000000)
    '''

    def get_drink_location(self):
        """Get the target position for a robot based on its index.

        Args:
            i (int): The index of the robot.

        Returns:
            target_position (tuple): A tuple representing the target row and column coordinates.
        """
        
        return random.choice([(9,9),(9,0),(0,9),(0,0)])

    def get_drink_name(self):

        name = random.choice(self.all_names)
        if name not in self.chosen_names:
            self.chosen_names.append(name)
            return name
        else:
            return self.get_drink_name()

        
        
        
        
