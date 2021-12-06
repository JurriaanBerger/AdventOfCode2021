file = open('data1.txt',"r")
f = file.read()
measurements_str = f.split("\n")
measurements = []

for s in measurements_str :
    measurements.append(int(s))

file.close()

print(measurements)

prev_measurement = 10000
increase_count = 0

for m in measurements:
    if int(m) > prev_measurement:
        increase_count+=1
    prev_measurement = int(m)
    # print(m,increase_count)

print (increase_count)

increase_count = 0

for i in range(len(measurements)-3):
    sum1 = measurements[i]+measurements[i+1]+measurements[i+2]
    sum2 = measurements[i+1]+measurements[i+2]+measurements[i+3]

    if sum1<sum2: increase_count+=1

print (increase_count)