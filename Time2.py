import math

total = int(input('Seconds: '))
times = [86400,3600,60,1]
tally = []
tallyb = []
names = ['',':',':',':']
for time in times:
    tally.append(math.floor(total/time))
    total -= math.floor(total/time) * time
for i,value in enumerate(tally):
    if value < 10 and i!=0:
        value = '0' + str(value)
    tallyb.append(value)

print(names[0] + str(tallyb[0]) + names[1] + str(tallyb[1]) + names[2] + str(tallyb[2]) + names[3] + str(tallyb[3]))