#Part 1: Find which outer bags could contain a 'shiny gold' bag

def neighbors(x,y):
    drow = [-1,0,1]
    dcol = [-1,0,1]
    
    [('.','Floor'),('L','EmptySeat'),('#','FullSeat')]
    # if Seat=Empty & All neighbors = Empty, Seat=Occ
    # if Seat=Occ & count(neighbors) >= 4, Seat=Empty
    
    return new_state


def main(start=''):
    #global winners
        
    with open(r'C:\Users\pjsmole\Documents\GitHub\AOC2020\AOC2020_11.inp','r') as f:
        inp = f.readlines()
    
    inp2 = [list(line.rstrip('\n')) for line in inp]
    inp3 = [line.insert(0,'.').append('.') for line in inp3]
    pad = ['.' for i in inp3[0]]
    seats = inp3.insert(0,pad).append(pad)
    
    timestep = 0
    changeflag = True
    while changeflag:
	    timestamp += 1
	    
	    for row in seats[1:-1]:
		    for col in row[1:-1]:
			    
    #Answer 1
    
    #Answer 2
    
    
    print(f'Number of bags inside shiny gold is {bagcount}')

if __name__ == '__main__':
    main('posh brown')

