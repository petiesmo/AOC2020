#Part 1: Find which outer bags could contain a 'shiny gold' bag


def visit_children(parents_child_list, current_path):
    global drules
    global winners
    for child in parents_child_list:
        if child is None:
            return None
        elif child in set(winners):
            winners = set(winners) | set(current_path)
            winners.add(child)
            return None
        else:
            list(current_path).append(child)
            #print(current_path)
            visit_children(drules[child].keys(), tuple(current_path))
    return None

def count_children(parents_child_dict):
    global drules
    num_bags = 0
    for child in parents_child_dict.keys():
        if drules[child] is None:
            num_bags += int(parents_child_dict[child])
            return num_bags
        else:
            num_bags += int(parents_child_dict[child])*count_children(drules[child])
    return num_bags


def main(start='shiny gold'):
    global winners
    global drules
    
    with open(r'C:\Users\pjsmole\Documents\GitHub\AOC2020\AOC2020_7.inp','r') as f:
        inp = f.readlines()
    
    inp2 = [line.rstrip('.\n') for line in inp]
    inp3 = [rule.split(' bags contain ') for rule in inp2]
    inp4 = {rule[0]: rule[1].replace(' bags','').replace(' bag','') for rule in inp3}
    colormap = {c:3000+i for i,c in enumerate(inp4.keys())}
    unmap = {3000+i:c for i,c in enumerate(inp4.keys())}
    start_color = colormap[start]
    drules = {}
    for color in inp4.keys():
        if 'no other' in inp4[color]:
            drules[colormap[color]] = {}
        else:
            temp = inp4[color].split(', ')
            temp2 = [child.split(' ',1) for child in temp]
            drules[colormap[color]] = {colormap[b]:a for [a,b] in temp2}
    print(drules[start_color])

    winners = set()
    winners.add(colormap['shiny gold'])

    for cstart in drules.keys():
        path = set()
        path.add(cstart)
        visit_children(drules[cstart].keys(), path)

    print([unmap[w] for w in set(winners)])
    print(f'Number of outer bags = {len(winners)-1}')

    #Answer 2
    
    bagcount = count_children(drules[colormap['shiny gold']])
    print(f'Number of bags inside shiny gold is {bagcount}')

if __name__ == '__main__':
    main('posh brown')

