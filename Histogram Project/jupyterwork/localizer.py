# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    
    for i in range(0, len(beliefs)):
        new_beliefs.append([])
        for k in range(0,len(beliefs[i])):
            if (color == grid[i][k]):
                new_beliefs[i].append(beliefs[i][k] * p_hit)
            else:
                new_beliefs[i].append(beliefs[i][k] * p_miss)
    new_beliefs = normalize(new_beliefs)
    
    return new_beliefs

def normalize(beliefs):
    sumtotal = 0
    for i in range(0, len(beliefs)):
        sumtotal = sumtotal + sum(beliefs[i])
    
    for k in range(0, len(beliefs)):
        for j in range(0, len(beliefs[k])):
            beliefs[k][j] = beliefs[k][j] / sumtotal
        
    return beliefs              

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(height)] for j in range(width)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)