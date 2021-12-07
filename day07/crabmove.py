import numpy as np


def read_crab():
    file = open('crabs.txt', "r")
    f1 = file.read()
    file.close()

    str_numbers = f1.split(",")
    num = []
    for n in str_numbers: num.append(int(n))

    return num


# Not sure about this step,
# but I claim that it is sufficient to only look at positions where currently a crab is positioned
# This operation takes O(n^2) time, however, it limits the number of computations done at a later stage
# Turns out: it works for part 1, not for part 2 (which makes sense)
def unique_positions(positions):
    uniq_pos = []
    for p in positions:
        if p not in uniq_pos:
            uniq_pos.append(p)
    return uniq_pos


# Cost calculation for part 1
def calc_cost(positions,goal_position):
    np_goal = np.ones(len(positions))*goal_position
    movement = positions-np_goal
    cost = np.sum(np.absolute(movement))
    return cost


# Cost calculation for part 2
def calc_cost2(positions,goal_position,lookup_table):
    np_goal = np.ones(len(positions)) * goal_position
    movement = positions - np_goal
    abs_movement = np.absolute(movement)
    cost = 0
    for m in abs_movement:
        cost += lookup_table[int(m)]
    return cost


# Calculating the cost for each crab individually, using recursion (in part 2) did not work out.
# You will reach the max. recursion depth
def calc_fuel_crab(movement):
    if movement == 0: return 0
    fuel = movement + calc_fuel_crab(movement-1)
    return fuel


# Use a lookup table instead. On beforehand calculate the cost of a movement of distance(x), for all possible x.
# By means of Dynamic Programming (i.e. using the result of x-1 for calculating x)
# Subsequently, when calculating the amount of fuel needed for a movement of distance y,
# you can just look in this table what the amount of fuel is
def create_fuel_lookup(lookup_table):
    for i in range(1,len(lookup_table)):
        lookup_table[i] = lookup_table[i-1]+i
    return lookup_table


# Setup
crab_positions = read_crab()
unique_crab_positions = unique_positions(crab_positions)
print(len(crab_positions),len(unique_crab_positions)) # the difference in length, thus what we save by using unique crab positions (in part 1)

np_crab_positions = np.array(crab_positions)


# Part 1
opt_pos = 0
opt_cost = calc_cost(np_crab_positions,0)

for u in unique_crab_positions:
    this_cost = calc_cost(np_crab_positions,u)
    if this_cost<opt_cost:
        opt_cost = this_cost
        opt_pos = u

print('ANSWER 1:', opt_cost)


# Part 2
fuel_lookup = np.zeros(max(crab_positions)-min(crab_positions)+1)
fuel_lookup = create_fuel_lookup(fuel_lookup)

opt_pos2 = 0
opt_cost2 = calc_cost2(np_crab_positions,0,fuel_lookup)

for u in range(min(crab_positions),max(crab_positions)):
    this_cost = calc_cost2(np_crab_positions,u,fuel_lookup)
    if this_cost<opt_cost2:
        opt_cost2 = this_cost
        opt_pos2 = u

print('ANSWER 2:', opt_cost2)