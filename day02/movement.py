file = open('data.txt',"r")
f = file.read()

input = f.split("\n")
input_data = []

pos_h = 0
pos_v = 0
aim = 0

for i in input:
    x = i.split(" ")
    print(x)
    if x[0] == 'forward':
        pos_h += int(x[1])
        pos_v += aim*int(x[1])
    elif x[0] == 'down' :
        # pos_v += int(x[1])
        aim += int(x[1])
    else:
        # pos_v -= int(x[1])
        aim -= int(x[1])
    print(pos_h,pos_v)

print('ANSWER: ',pos_h*pos_v)