# Built in variable values

import random
identifier = 1000
grid_size = 10

# User defiend variable values and introduction message

name = input('What is the name of the robot? ')



# Random allocation of starting position 

row_coordinate = random.randint(0, (grid_size - 1))
column_coordinate = random.randint(0,(grid_size - 1))

# Random allocation of starting direction. Created variable 'direction_list' as the output of the random sample is a list. 

directions = ['North','South','East','West']
direction_list = random.sample(directions,1)
direction = direction_list[0]

# Deduction of starting quadrant. Boundary defined as <= (grid size/2 - 1) given starting coordinate of 0.

'''
if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'
'''

# The robot talks

print(f"Hello. My name is {name}. My ID is {identifier}")
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.") # I am in the {location} quadrant.

# Statement of starting direction given n,s,e,w input.
# Could create dictionary. Or randomly sample the words not the letters??

'''
if direction == 'n':
    print('I am facing North')
elif direction == 's':
    print('I am facing South')
elif direction == 'e':
    print('I am facing East')
else:
    print('I am facing West')
'''

# Moving to edge of grid, one step at a time

while row_coordinate != (grid_size - 1) or column_coordinate != (grid_size - 1):

    if direction == 'North':
        while row_coordinate != 0:
            print('Moving one step forward') 
            row_coordinate -= 1
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
        if row_coordinate == 0:
            print('I have a wall in front of me')
            print('Turning 90 degrees clockwise')
            direction = 'East'
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
    elif direction == 'South':
        while row_coordinate != (grid_size - 1):
            print('Moving one step forward') 
            row_coordinate += 1
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
        if row_coordinate == (grid_size - 1):
            print('I have a wall in front of me')
            print('Turning 90 degrees clockwise')
            direction = 'West'
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
    elif direction == 'East':
        while column_coordinate != (grid_size - 1):
            print('Moving one step forward') 
            column_coordinate += 1
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
        if column_coordinate == (grid_size - 1):
            print('I have a wall in front of me')
            print('Turning 90 degrees clockwise')
            direction = 'South'
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
    elif direction == 'West':
        while column_coordinate != 0:
            print('Moving one step forward') 
            column_coordinate -= 1
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")
        if column_coordinate == 0:
            print('I have a wall in front of me')
            print('Turning 90 degrees clockwise')
            direction = 'North'
            print(f"My current location is ({row_coordinate}, {column_coordinate}). I am facing {direction}.")

print('I am drinking leché, I am happy!')




# Deduction of new quadrant.
# Repeated code, could build a function..
'''
if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'
'''
 









