import numpy as np


# This should return [x1,y1,x2,y2]
def read_lines():
    file = open('lines.txt', "r")
    f1 = file.read()
    file.close()
    f1 = f1.replace(' -> ',',')
    f2 = f1.split('\n')

    input_data = []
    for f in f2:
        g = f.split(',')
        input_data.append([int(c) for c in g])

    return input_data


def is_diagonal(point1,point2):
    # print('CHECK',point1,point2)
    if abs(point1[0]-point2[0]) == abs(point1[1]-point2[1]): return True
    return False


# This adds a line to the field
def add_line(this_field,line,diagonal):
    # vertical line (x's are the same)
    if line[0] == line[2]:
        for i in range(min(line[1],line[3]),max(line[1],line[3])+1):
            this_field[i,line[0]] = this_field[i,line[0]]+1

    # horizontal line (y's are the same)
    elif line[1] == line[3]:
        for i in range(min(line[0],line[2]),max(line[0],line[2])+1):
            this_field[line[1],i] = this_field[line[1],i]+1

    #else: print(is_diagonal([line[0],line[1]],[line[2],line[3]]))
    elif diagonal and is_diagonal([line[0],line[1]],[line[2],line[3]]):
        if line[0] < line[2]:
            start = [line[0],line[1]]
            end = [line[2]+1,line[3]+1]
        else:
            start = [line[2], line[3]]
            end = [line[0] + 1, line[1] + 1]

        # print('DIAG:',start,end)

        # decreasing horizontally
        if start[1] > end[1]:
            for i in range(start[0],end[0]):
                # print('MARK DO:',[i, start[1]+start[0]-i])
                this_field[start[1]+start[0]-i,i] = this_field[start[1]+start[0]-i,i] + 1
        # increasing horizontally
        else:
            for i in range(start[0],end[0]):
                # print('MARK UP:', [i, start[1]-start[0]+i])
                this_field[start[1]-start[0]+i,i] = this_field[start[1]-start[0]+i,i] + 1

    return this_field


# Read the input
lines = read_lines()

# Determine size of the field
field_size = 0
for l in lines:
    max_l = max(l)
    if max_l > field_size: field_size = max_l
field = np.zeros([field_size+1,field_size+1])

for l in lines:
    add_line(field,l,False)

print('ANSWER 1:',len(np.argwhere(field >= 2)))

# Part 2
field_2 = np.zeros([field_size+1,field_size+1])

for l in lines:
    add_line(field_2,l,True)
    #print(l)
    #print(field_2)
print('ANSWER 2:',len(np.argwhere(field_2 >= 2)))