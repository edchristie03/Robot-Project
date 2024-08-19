import random
from drink import Drink

class DrinkFactory:

    def __init__(self, all_names, chosen_names=[]):
        """Constructor for DrinkFactory.

        Args:
            all_names (list): A list of all possible drink names.
            chosen_names (list): A list of names already chosen (default is empty).
        """
        self.all_names = all_names
        self.chosen_names = chosen_names
        pass

        
    def create_drinks(self, n_of_robots):
        """Creates a list of drinks for a given number of robots.

        Args:
            n_of_robots (int): Number of drinks to create (one per robot).

        Returns:
            drinks (list): A list of Drink objects.
        """
        drinks = []
        for i in range(n_of_robots):
            drink = self.set_up_drink()
            drinks.append(drink)

        return drinks

    def set_up_drink(self):
        """Sets up a new drink.

        Returns:
            drink (Drink): A Drink object with a randomly selected name.
        """
        name = self.get_drink_name()
        drink = Drink(name)

        return drink

    def get_drink_name(self):
        """Randomly selects a drink name that has not been used yet.

        Returns:
            name (str): The name of the drink.
        """
        name = random.choice(self.all_names)
        if name not in self.chosen_names:
            self.chosen_names.append(name)
            return name
        else:
            return self.get_drink_name()

        
        
        
        
