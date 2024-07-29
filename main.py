import random
identifier = 1000
grid_size = 10

name = input('What is the name of the robot? ')
message = f"Hello. My name is {name}. My ID is {identifier}"
print(message)

row_coordinate = random.randint(0, (grid_size - 1))
column_coordinate = random.randint(0,(grid_size - 1))

directions = ['n','s','e','w']
direction_list = random.sample(directions,1)
direction = direction_list[0]

if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'
 
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am in the {location} quadrant.")

if direction == 'n':
    print('I am facing North')
elif direction == 's':
    print('I am facing South')
elif direction == 'e':
    print('I am facing East')
else:
    print('I am facing West')

print('Moving one step forward')

if direction == 'n' and row_coordinate != 0:
    row_coordinate -= 1
elif direction == 's' and row_coordinate != (grid_size - 1):
    row_coordinate += 1
elif direction == 'e' and column_coordinate != (grid_size - 1):
    column_coordinate += 1
elif direction == 'w' and column_coordinate != 0:
    column_coordinate -= 1

if row_coordinate <= (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'top left'
elif row_coordinate <= (grid_size/2 - 1) and column_coordinate > (grid_size/2 - 1):
    location = 'top right'
elif row_coordinate > (grid_size/2 - 1) and column_coordinate <= (grid_size/2 - 1):
    location = 'bottom left'
else:
    location = 'bottom right'
 
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am in the {location} quadrant.")









