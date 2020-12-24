#Part 1: Find how many time steps until equilibrium reached
from copy import deepcopy
from pprint import pprint

class Seats():
	def __init__(self,rows,cols):
		self.grid = [['.' for c in range(cols+2)] for r in range(rows+2)]
		self.rows = rows
		self.cols = cols
		
	@property
	def seat(self,r,c):
		return self.grid[r][c]
	
	def pad(self,numr=1,numc=1):
		inp3 = [line.insert(0,'.').append('.') for line in self.grid]
	    pad = ['.' for i in inp3[0]]
	    self.grid = inp3.insert(0,pad).append(pad)
	    return None
	
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
	    
    #[('.','Floor'),('L','EmptySeat'),('#','FullSeat')]
    # if Seat=Empty & All neighbors = Empty, Seat=Occ
    # if Seat=Occ & count(neighbors) >= 4, Seat=Empty


def main(start=''):
    #global winners
        
    with open(r'C:\Users\pjsmole\Documents\GitHub\AOC2020\AOC2020_11.inp','r') as f:
        inp = f.readlines()
    
    inp2 = [list(line.rstrip('\n')) for line in inp]
    
    rows,cols = len(inp2), len(inp2[0])
    seats = Seats(rows,cols)
    seats.grid = [[c for c in inp2[r]] for r in inp2]
    seats.pad()
    
    timestep = 0
    images = []
    images.append(seats)
    changeflag = True
    
    while changeflag:
	    changeflag = False
	    timestep += 1
	    oldseats = images[-1]
	    newseats = Seats(rows,cols).pad()
	    
	    for r,row in enumerate(oldseats.grid[1:-1], start=1):
		    for c,col in enumerate(row[1:-1], start=1):
			    spot = oldseats.seat(r,c)
			    nbrs = oldseats.num_neighbors(r,c)
			    if spot == '.':
				    pass
				elif spot == 'L' and nbrs == 0:
					newseats.grid[r][c] = '#'
					changeflag = True
				elif spot == '#' and nbrs>= 4:
					newseats.grid[r][c] = 'L'
					changeflag = True
					
		images.append(newseats)
		
    #Answer 1
    print(f'Equilibrium reached in {timestep} steps')
    #Answer 2
    

if __name__ == '__main__':
    main()

