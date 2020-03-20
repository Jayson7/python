def squaresBelow(upperBound=0):
    x=1
    while 1:
        yield map(lambda x:x**2, range(x,0,-1))
        x +=1
        if x > upperBound: return squaresBelow()