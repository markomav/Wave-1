import math
try:
    cash = int(input("$ in cents given: "))
    coins = [200,100,25,10,5,1]
    tally = []
    names = ['toonies: ',', loonies: ',', quarters: ',', dimes: ',', nickels: ',', pennies: ']
    for coin in coins:
        tally.append(math.floor(cash/coin))
        cash -= math.floor(cash/coin) * coin
    print(names[0] + str(tally[0]) + names[1] + str(tally[1]) + names[2] + str(tally[2]) + names[3] + str(tally[3]) + names[4] + str(tally[4]) + names[5] + str(tally[5]))
except Exception:
    print('You cannot give me words only money!')
    pass