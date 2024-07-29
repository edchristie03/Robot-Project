name = input('What is the name of the robot? ')
identifier = 1000
message = f"Hello. My name is {name}. My ID is {identifier}"
print(message)

grid_size = 10

row_coordinate = int(input('What is its current row coordinate? '))
column_coordinate = int(input('What is its current column coordinate? '))

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
