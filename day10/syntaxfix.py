def read_syntax_input():
    file = open('brackets.txt', "r")
    f1 = file.read()
    file.close()
    f2 = f1.split('\n')

    return f2


def find_corrupted(line):
    to_close=[]

    for l in line:
        if l in ['{','[','<','(']:
            to_close.append(l)
        else:
            should_match = to_close[-1]
            if should_match == '{' :
                if l !='}':
                    return True, l
                else: to_close.pop(-1)
            elif should_match == '[':
                if l != ']':
                    return True, l
                else:
                    to_close.pop(-1)
            elif should_match == '<':
                if l != '>':
                    return True, l
                else:
                    to_close.pop(-1)
            else:
                if l != ')':
                    return True, l
                else:
                    to_close.pop(-1)

    return False, ' '


def complete(line):
    to_close=[]

    for l in line:
        if l in ['{', '[', '<', '(']:
            to_close.append(l)
        else: to_close.pop(-1)

    score = 0
    while len(to_close)>0:
        x = to_close.pop(-1)
        if x == '(':
            line= line+')'
            score = score*5+1
        elif x == '[':
            line= line+']'
            score = score * 5 + 2
        elif x == '{':
            line= line+'}'
            score = score * 5 + 3
        else:
            line= line+'>'
            score = score * 5 + 4

    return score


# Part 1 (and a bit of part 2, discarding the corrupted lines)
syntax = read_syntax_input()
points = 0
no_corrupt_syntax = []

for s in syntax:
    corrupt, char = find_corrupted(s)
    if corrupt and char == ')': points += 3
    if corrupt and char == ']': points += 57
    if corrupt and char == '}': points += 1197
    if corrupt and char == '>': points += 25137
    if not corrupt: no_corrupt_syntax.append(s)

print('ANSWER 1:', points)

scores = []
for s in no_corrupt_syntax:
    scores.append(complete(s))

print(scores[0])
scores.sort()
print(scores[0])

print(len(scores),round((len(scores)-1)/2))
print('ANSWER 2:', scores[round((len(scores)-1)/2)])