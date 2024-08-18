
class Drink:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Drink of {self.name} at location {self.location}."


