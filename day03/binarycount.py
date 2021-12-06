import numpy as np

file = open('data.txt',"r")
f = file.read()

input = f.split("\n")
input_data = []

for i in input:
    input_data.append ([int(c) for c in i])


def count (bites):
    counter = np.zeros(len(bites[0]))
    for b in bites:
        counter += b
    return counter


def convert_to_dec(binary):
    dec = 0
    power = len(binary)-1
    for b in binary:
        dec += b*(2**power)
        power -=1
    return dec


count_ones = count(input_data)

print('COUNT ONES:',count_ones)

gamma_rate = np.zeros(len(input_data[0]))

for k in range(len(count_ones)):
    if count_ones[k] > (len(input_data)/2): gamma_rate[k] = 1

print('GAMMA RATE:',gamma_rate)

epsilon_rate = np.ones(len(input_data[0])) - gamma_rate
print('EPS RATE:  ',epsilon_rate)

dec_gamma = convert_to_dec(gamma_rate)
dec_eps = convert_to_dec(epsilon_rate)

print('ANSWER 1',dec_gamma*dec_eps)


# Part 2


def select(bites, position, most):
    bites1=[]
    bites0=[]
    count1 = 0

    for b in bites:
        if b[position] == 1:
            count1 +=1
            bites1.append(b)
        else: bites0.append(b)

    if most:
        if count1 >= len(bites)/2 :
            bites=bites1
        else:
            bites=bites0
    else :
        if count1 < len(bites)/2 :
            bites=bites1
        else:
            bites=bites0

    # there is more than one candidate and the position is smaller than the number of bites
    if len(bites)>1 and position<(len(bites[0])-1):
        return select(bites,position+1,most)

    # there is just one candidate (if the position is bigger than the number of bites something went wrong)
    else :
        return bites


ox_rating = select(input_data,0,True)
print('OX:', ox_rating)
ox_dec = convert_to_dec(ox_rating[0])
print(ox_dec)

co_rating = select(input_data,0,False)
print('CO:',co_rating)
co_dec = convert_to_dec(co_rating[0])
print(co_dec)

print('ANSWER 2',ox_dec*co_dec)