identifier = 1000
grid_size = 10

name = input('What is the name of the robot? ')
row_coordinate = int(input('What is its current row coordinate? '))
column_coordinate = int(input('What is its current column coordinate? '))
direction = input('What direction is the robot facing? (n,s,e,w) ')

message = f"Hello. My name is {name}. My ID is {identifier}"
print(message)

if row_coordinate > (grid_size - 1):
    row_coordinate = (grid_size - 1)
elif row_coordinate < 0:
    row_coordinate = 0

if column_coordinate > (grid_size - 1):
    column_coordinate = (grid_size - 1)
elif column_coordinate < 0:
    column_coordinate = 0

if row_coordinate <= 4 and column_coordinate <= 4:
    location = 'top left'
elif row_coordinate <=4 and column_coordinate >=5:
    location = 'top right'
elif row_coordinate >=5 and column_coordinate <= 4:
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

if row_coordinate <= 4 and column_coordinate <= 4:
    location = 'top left'
elif row_coordinate <=4 and column_coordinate >=5:
    location = 'top right'
elif row_coordinate >=5 and column_coordinate <= 4:
    location = 'bottom left'
else:
    location = 'bottom right'
 
print(f"My current location is ({row_coordinate}, {column_coordinate}). I am in the {location} quadrant.")









