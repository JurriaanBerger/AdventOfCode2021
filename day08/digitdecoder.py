def read_input():
    signal_patterns = []
    output_values = []
    with open('digits.txt',"r") as f:
        for line in f:
            l = line.strip()
            l = l.split(" | ")
            signal_patterns.append(l[0].split(' '))
            output_values.append(l[1].split(' '))

    print(output_values)
    return signal_patterns, output_values


def find_strings(output_values):
    counter = 0
    for i in range(len(output_values)):
        for j in range(len(output_values[i])):
            this_length = len(output_values[i][j]) # limit the number of times the 'len' function is used
            if this_length == 2 or this_length == 3 or this_length == 4 or this_length == 7:
                counter += 1

    return counter


def difference(str_a,str_b):
    if len(str_a) < len(str_b):
        str_c = str_a
        str_a = str_b
        str_b = str_c
    diff = ''
    for s in str_a:
        if s not in str_b: diff += s
    return diff


def find_encoding(input_signal):
    encoding = {}
    for i in input_signal:
        this_length = len(i)
        if this_length == 2: encoding["1"] = i
        elif this_length == 3: encoding["7"] = i
        elif this_length == 4: encoding["4"] = i
        elif this_length == 7: encoding["8"] = i

    real_a = difference(encoding["1"],encoding["7"])

    # For finding other encodings, it all comes down to how many characters they differ

    # 5 is the string that contains 3 characters from 4, and contains real_a
    # if the strings do not match the 5, they might match another number
    five_candidate = encoding["4"]+real_a
    for j in input_signal:
        if len(j) == 5:
            if len(difference(j,encoding["1"])) == 4:
                if len(difference(j,five_candidate)) == 1:
                    encoding["5"] = j
                else:
                    encoding["2"] = j
            else:
                encoding["3"] = j
        elif len(j) == 6:
            if len(difference(j,encoding["4"])) == 2:
                encoding["9"] = j
            elif len(difference(j,encoding["7"])) == 4:
                encoding["6"] = j
            else: encoding["0"] = j

    return encoding


# Find the right encoding for the output value.
# Which is essentially to see which encoding has no difference with the value.

# In order to limit the usage of my not so efficient difference function:
# first check if the length of the two are the same.
# Because if this is not the case, they will differ at least one character.
# Off course, this is not necessary to do.

def translate_output(encoding, output_values):
    number = ''
    for c in output_values:
        for e in encoding:
            enc = encoding[e]
            if len(enc) == len(c) and len(difference(enc,c)) == 0:
                number += e
    return int(number)


signal, output = read_input()

# Part 1
print('ANSWER 1:',find_strings(output))


# Part 2
output_sum = 0
for i in range(len(signal)):
    this_encoding = find_encoding(signal[i])
    output_sum += translate_output(this_encoding, output[i])

print('ANSWER 2:',output_sum)