#Part 1: Find how many time steps until equilibrium reached
from copy import deepcopy
from pprint import pprint

class Seats():
	def __init__(self,rows,cols):
		self.grid = [['.' for c in range(cols+2)] for r in range(rows+2)]
		self.rows = rows
		self.cols = cols
		
	def seat(self,r,c):
		return self.grid[r][c]
	
	def num_neighbors(self,r,c):
		count = 0
		for drow in [-1,0,1]:
			for dcol in [-1,0,1]:
				if drow==dcol==0:
					pass
				else:
					if self.grid[r+drow][c+dcol] == '#':
						count += 1
		return count
	
	
	def num_los(self,r,c):
		countlos = 0
		for drow in [-1,0,1]:
			for dcol in [-1,0,1]:
				if drow == dcol == 0:
					pass
				else:
					erow,ecol = r,c
					while True:
						erow += drow
						ecol += dcol
						if erow == 0 or ecol == 0 or erow == self.rows+1 or ecol == self.cols+1:
							break
						if self.seat(erow,ecol) == '#':
							countlos += 1
							break
						
					
		return countlos
			
			
	def num_occ(self):
		count = 0
		for r in self.grid:
			for c in r:
				if c == '#':
					count += 1
		return count
		
		
	def show(self):
		pprint([''.join(r) for r in self.grid])
		return None
		
#[('.','Floor'),('L','EmptySeat'),('#','FullSeat')]
# if Seat=Empty & All neighbors = Empty, Seat=Occ
# if Seat=Occ & count(neighbors) >= 4, Seat=Empty


def main(start=''):
    #global winners
        
    with open(r'AOC2020_11a.inp','r') as f:
        inp = f.readlines()
	    #C:\Users\pjsmole\Documents\GitHub\AOC2020\
    inp2 = [list(line.rstrip('\n')) for line in inp]
    
    rows,cols = len(inp2), len(inp2[0])
    seats = Seats(rows,cols)
    for r,row in enumerate(inp2,1):
	    for c,col in enumerate(row,1):
		    seats.grid[r][c] = col
    #seats.show()
    #seats.pad()
    
    timestep = 0
    images = []
    images.append(seats)
    changeflag = True
    
    while changeflag:
	    changeflag = False
	    timestep += 1
	    oldseats = images[-1]
	    newseats = Seats(rows,cols)
	    for r,row in enumerate(oldseats.grid[1:-1], start=1):
		    for c,col in enumerate(row[1:-1], start=1):
			    spot = oldseats.seat(r,c)
			    nbrs = oldseats.num_neighbors(r,c)
			    if spot == '.':
				    pass
			    elif spot == 'L':
				    if nbrs == 0:
					    newseats.grid[r][c] = '#'
					    changeflag = True
				    else:
					    newseats.grid[r][c] = 'L'
			    
			    elif spot == '#':
				    if nbrs>= 4:
					    newseats.grid[r][c] = 'L'
					    changeflag = True
				    else:
					    newseats.grid[r][c] = '#'
			    else:
				    print(f'Somethings not right at {timestep}, {row,col}')
	    images.append(newseats)
	    print(f'Time: {timestep} Occ: {newseats.num_occ()}')
	    #newseats.show()
		
    #Answer 1
    print(f'Equilibrium reached in {timestep} steps')
    #Answer 2
    

if __name__ == '__main__':
    main()

