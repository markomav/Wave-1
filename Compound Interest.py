def interest(P):
    I = 1.04
    A1 = P * I**1
    A2 = P * I**2
    A3 = P * I**3
    return('1st Year: $' + str(A1*100//1/100) + ', 2nd Year: $' + str(A2*100//1/100) + ', 3rd Year: $' + str(A3*100//1/100))