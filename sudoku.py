rows = "ABCDEFGHI"
cols = "123456789"

def cross(a,b):
	return [s+t for s in a for t in b]

boxes = cross(rows,cols)

row_units = [cross(r, cols) for r in rows]

column_units = [cross(rows, c) for c in cols]

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

unitlist = row_units + column_units + square_units
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):

	return dict(zip(boxes,grid))

a = grid_values(grid)
print(a)

#def display(values):



