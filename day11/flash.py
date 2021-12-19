import numpy as np


def read_octo():
    octo_map = []

    file = open('octo.txt', "r")
    f1 = file.read()
    file.close()

    f2 = f1.split("\n")

    for h in f2:
        list_h = []
        list_h[:0] = h
        octo_map.append([int(l) for l in list_h])

    return np.array(octo_map)


def energy_increase(cur_energy_map):
    new_energy_map = cur_energy_map + np.ones([len(cur_energy_map), len(cur_energy_map)])
    return new_energy_map


def find_flash(cur_energy_map,flashed_map):
    i = 0

    while i < len(cur_energy_map[0]):
        flashed = False
        for j in range(len(cur_energy_map)):
            if flashed_map[i, j] == 0 and cur_energy_map[i, j] > 9:
                flashed = True
                flashed_map[i, j] = 1
                for p in range(max(i - 1, 0), min(i + 2,len(cur_energy_map))):
                    for q in range(max(j - 1, 0), min(j + 2, len(cur_energy_map))):
                        if flashed_map[p, q] == 0: cur_energy_map[p, q] += 1
                break

        if flashed: i = 0
        else: i += 1

    return cur_energy_map, flashed_map


def reset_flashed(cur_energy_map, flashed_map):
    to_subtract = cur_energy_map*flashed_map
    new_energy_map = cur_energy_map-to_subtract
    return new_energy_map


# Part 1
energy_map = read_octo()

total_sum = 0
for e in range(0, 100):
    energy_map_increase = energy_increase(energy_map)
    did_flash_map = np.zeros([len(energy_map), len(energy_map)])
    energy_map, did_flash_map = find_flash(energy_map_increase, did_flash_map)
    energy_map = reset_flashed(energy_map, did_flash_map)
    total_sum += np.sum(did_flash_map)


print('ANSWER 1:', total_sum)


# Part 2
energy_map = read_octo()
did_flash_map = np.zeros([len(energy_map), len(energy_map)])

step_counter = 0
while np.sum(did_flash_map) < 100:
    energy_map_increase = energy_increase(energy_map)
    did_flash_map = np.zeros([len(energy_map), len(energy_map)])
    energy_map, did_flash_map = find_flash(energy_map_increase, did_flash_map)
    energy_map = reset_flashed(energy_map, did_flash_map)
    step_counter += 1

print('ANSWER 2:', step_counter)
