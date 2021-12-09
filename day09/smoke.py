import numpy as np

def read_heightmap():
    heigtmap = []

    file = open('map.txt', "r")
    f1 = file.read()
    file.close()

    f2 = f1.split('\n')

    for h in f2:
        list_h = []
        list_h[:0] = h
        heigtmap.append([int(l) for l in list_h])

    return heigtmap


def find_max_height(heightmap):
    max_height = 0
    for h in heightmap:
        max_h = max(h)
        if max_h > max_height: max_height = max_h
    return max_height


def add_padding(heightmap,max_height):
    new_map = np.ones([len(heightmap)+2,len(heightmap[0])+2])*max_height

    for i in range(len(heightmap)):
        new_map[i+1,1:-1] = np.array(heightmap[i])

    return new_map


def count_minima(heightmap):
    counter = 0
    risk_level = 0
    for i in range(1,len(heightmap)-1):
        for j in range(1,len(heightmap[i])-1):
            this_value = heightmap[i][j]
            if heightmap[i][j+1] > this_value and heightmap[i][j-1] > this_value and heightmap[i+1][j] > this_value and heightmap[i-1][j] > this_value:
                counter += 1
                risk_level += (1+this_value)
    return risk_level


def find_basin_border(heightmap,max_height):
    border_map = heightmap-max_height
    return border_map


def basin_size(border_map,checked_map,start_x,start_y):

    size = 1
    checked_map[start_x,start_y] = 1
    if border_map[start_x+1,start_y] < 0 and checked_map[start_x+1,start_y] == 0:
        add_size,checked_map = basin_size(border_map,checked_map,start_x+1,start_y)
        size += add_size

    if border_map[start_x - 1, start_y] < 0 and checked_map[start_x - 1, start_y] == 0:
        add_size,checked_map = basin_size(border_map, checked_map, start_x - 1, start_y)
        size += add_size

    if border_map[start_x, start_y + 1] < 0 and checked_map[start_x, start_y + 1] == 0:
        add_size,checked_map = basin_size(border_map, checked_map, start_x, start_y + 1)
        size += add_size

    if border_map[start_x, start_y - 1] < 0 and checked_map[start_x, start_y - 1] == 0:
        add_size,checked_map = basin_size(border_map, checked_map, start_x, start_y - 1)
        size += add_size

    return size,checked_map # returns the size of the bassin and the updated checked map


def all_basin_sizes(border_map):
    checked = np.zeros([len(border_map),len(border_map[0])])
    largest = np.array([-1,-2,-3])

    for i in range(1,len(border_map)-1):
        for j in range(1,len(border_map[i])-1):
            if border_map[i][j] < 0 and checked[i][j] == 0:
                this_size, checked = basin_size(border_map,checked,i,j)
                if this_size >= min(largest):
                    ind = np.argmin(largest)
                    largest[ind] = this_size

    largest_value = largest[0]*largest[1]*largest[2]

    return largest_value


map = read_heightmap()
map_max_height = find_max_height(map)
map_pad = add_padding(map,map_max_height)


# Part 1
print('ANSWER 1:',count_minima(map_pad))


# Part 2
# task is to find the boundaries of the max value
map_basin_borders = find_basin_border(map_pad,map_max_height)
print('ANSWER 2:',all_basin_sizes(map_basin_borders))