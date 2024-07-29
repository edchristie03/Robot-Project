# Built in variable values

import random
identifier = 1000
grid_size = 10

# User defiend variable values and introduction message

name = input('What is the name of the robot? ')
message = f"Hello. My name is {name}. My ID is {identifier}"
print(message)

# Random allocation of starting position 

row_coordinate = random.randint(0, (grid_size - 1))
column_coordinate = random.randint(0,(grid_size - 1))

# Random allocation of starting direction. Created variable 'direction_list' as the output of the random sample is a list. 

directions = ['n','s','e','w']
direction_list = random.sample(directions,1)
direction = direction_list[0]

# Deduction of starting quadrant. Boundary defined as <= (grid size/2 - 1) given starting coordinate of 0.

if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'

# Statement of starting position
 
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am in the {location} quadrant.")

# Statement of starting direction given n,s,e,w input.
# Could create dictionary. Or randomly sample the words not the letters??

if direction == 'n':
    print('I am facing North')
elif direction == 's':
    print('I am facing South')
elif direction == 'e':
    print('I am facing East')
else:
    print('I am facing West')

# Moving one step forward if grid size allows

print('Moving one step forward') 

if direction == 'n' and row_coordinate != 0:
    row_coordinate -= 1
elif direction == 's' and row_coordinate != (grid_size - 1):
    row_coordinate += 1
elif direction == 'e' and column_coordinate != (grid_size - 1):
    column_coordinate += 1
elif direction == 'w' and column_coordinate != 0:
    column_coordinate -= 1

# Deduction of new quadrant.
# Repeated code, could build a function..

if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'
 
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am in the {location} quadrant.")









