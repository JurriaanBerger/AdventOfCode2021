# For analyzing time complexity
# n1: number of fish (at the start)
# n2: number of fist (at the end)
# m: number of days
# k: longest timer (almost constant)

import numpy as np


def read_fish():
    file = open('fish.txt', "r")
    f1 = file.read()
    file.close()

    str_numbers = f1.split(",")
    num = []
    for n in str_numbers: num.append(int(n))

    return num


# Lower all timers by one

def day(fish_list):
    fish_list = fish_list - np.ones(len(fish_list))
    return fish_list


# Check how many fish have a timer of 0's and create a list of 8's with this length
# You cannot concatenate these immediately, as the 'current' fish still need their timer to be updated
# Although that could be avoided by counting -1's instead of 0's

def new_fish(fish_list):
    num_new_fish = len(fish_list)-np.count_nonzero(fish_list)
    add_fish = np.ones(num_new_fish)*8
    return add_fish


# All fish that reached got -1 on their timer should be reset to 6

def restart_fish(fish_list):
    for f in range(len(fish_list)):
        if fish_list[f] == -1.0:
            fish_list[f]=6.0

    return fish_list


# For part 2: Initialize by converting the list of all fish to a list with counters per day
# Basically the principle of 'bagging':
# you count how many fish there are in the 'bag' of fish with a timer of 0/1/... days

def convert(fish_list):
    counter = np.zeros(9)
    for f in fish_list:
        counter[int(f)] = counter[int(f)] + 1
    return counter


# Instead of having to change/reset the timers for all fish individually, just move the #fish in the 'bag' of timer=4
# to the bag of timer=3.
# For bag timer=0, we need to do the following:
# The number of fish in bag timer=0 is added to the bag of timer=6
# The number of fish in the bag timer=8 is set to the number of fish in the bag timer=0 (i.e. their offspring)

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

# For every day, update the timers and start the offspring
for i in range(1,81):
    to_add_fish = new_fish(fish)
    fish = day(fish)
    fish = restart_fish(fish)
    fish = np.append(fish, to_add_fish, axis=0)

print('ANSWER 1:',len(fish)) # total complexity: O(n2) (where n2 can be a very very big number)


# Part 2
fish_counter = convert(np.array(fish_arr))

# Do the 'move bags' and create offspring operation.
for i in range(1,81):
    fish_counter = shift(fish_counter)

# Count the number of fish in every bag.
total = 0
for f in fish_counter:
    total += f

print('ANSWER 2:',total) # total complexity: O(m)
