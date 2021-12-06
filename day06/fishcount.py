import numpy as np


def read_fish():
    file = open('fish.txt', "r")
    f1 = file.read()
    file.close()

    str_numbers = f1.split(",")
    num = []
    for n in str_numbers: num.append(int(n))

    return num


def day(fish_list):
    fish_list = fish_list - np.ones(len(fish_list))
    return fish_list


def new_fish(fish_list):
    num_new_fish = len(fish_list)-np.count_nonzero(fish_list)
    add_fish = np.ones(num_new_fish)*8
    return add_fish


def restart_fish(fish_list):
    for f in range(len(fish_list)):
        if fish_list[f] == -1.0:
            fish_list[f]=6.0

    return fish_list


def convert(fish_list):
    counter = np.zeros(9)
    for f in fish_list:
        counter[int(f)] = counter[int(f)] + 1
    return counter


def shift(counter):
    new_counter = np.zeros(9)
    for i in range(0,len(counter)-1):
        new_counter[i] = counter[i+1]
    new_counter[6] = new_counter[6]+counter[0]
    new_counter[8] = counter[0]
    return new_counter


fish_arr = read_fish()
fish = np.array(fish_arr)


# Part 1
# print('day 0',fish)
for i in range(1,81):
    to_add_fish = new_fish(fish)
    fish = day(fish)
    fish = np.append(fish, to_add_fish, axis=0)
    fish = restart_fish(fish)
    # print('day',i,fish)

print('ANSWER 1:',len(fish))


# Part 2
fish_counter = convert(np.array(fish_arr))

to_add = fish_counter[0]

for i in range(1,81):
    fish_counter = shift(fish_counter)

total = 0
for f in fish_counter:
    total += f

print('ANSWER 2:',total)
