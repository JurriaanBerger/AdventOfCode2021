import pandas as pd


def read_rules():
    file = open('rules.txt', "r")
    f1 = file.read()
    file.close()
    f2 = f1.split("\n")

    input_rules = {}

    for f in f2:
        r = f.split(' -> ')
        input_rules[r[0]] = r[1]

    return input_rules


def grow(string, rules):
    new_string = ''

    string_arr = list(string)
    new_string += string_arr[0]

    for i in range(1, len(string_arr)):
        pair = string_arr[i-1]+string_arr[i]
        insert = rules[pair]
        new_string += insert
        new_string += string_arr[i]

    return new_string


def smart_grow(pair_cntr, rules):
    new_pair_count = {}

    for p in pair_cntr:
        cnt = pair_cntr[p]
        add = rules[p]
        new_pair_l = p[0]+add
        new_pair_r = add+p[1]

        if new_pair_l in new_pair_count:
            new_pair_count[new_pair_l] += cnt
        else: new_pair_count[new_pair_l] = cnt

        if new_pair_r in new_pair_count:
            new_pair_count[new_pair_r] += cnt
        else: new_pair_count[new_pair_r] = cnt

    return new_pair_count


def count(string):
    counter = pd.Series(list(string)).value_counts()
    return pd.Series.max(counter)-pd.Series.min(counter)


def pair_count(string):
    pair_cnt = {}

    string_arr = list(string)
    for i in range(1, len(string_arr)):
        pair = string_arr[i - 1] + string_arr[i]
        if pair in pair_cnt:
            pair_cnt[pair] += 1
        else: pair_cnt[pair] = 1

    return pair_cnt


def char_count(pair_cntr, first_character):
    char_cnt = {}

    for p in pair_cntr:
        if p[1] in char_cnt:
            char_cnt[p[1]] += pair_cntr[p]
        else: char_cnt[p[1]] = pair_cntr[p]

    char_cnt[first_character] += 1

    print(char_cnt)

    ma = char_cnt[max(char_cnt, key=char_cnt.get)]
    mi = char_cnt[min(char_cnt, key=char_cnt.get)]

    return ma - mi


rules = read_rules()

# Part 1
string0 = 'SHPPPVOFPBFCHHBKBNCV'

for i in range(1,2):
    string_i = grow(string0, rules)
    string0 = string_i
    print(i)

print(count(string0))


# Part 2
string0 = 'SHPPPVOFPBFCHHBKBNCV'
count0 = pair_count(string0)
first_char = string0[0]
print(count0)

for i in range(1,41):
    count_i = smart_grow(count0, rules)
    count0 = count_i

print(char_count(count0,first_char))
