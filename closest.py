def brute_force(x,y):
    delta = 10000000
    xsmall = ysmall = 0
    for xiter in x:
        for yiter in y:
            dist = calcDist()
            #if delta > dist
                #xsmall = x
                #ysmall = y
    return [xsmall,ysmall]

def middle_helper(y,delta,midpoint):
    deltatemp = xnew = ynew = 0
    yprime = []#all y (whose x val) is within (midpoint+delta,midpoint-delta)
    for y in yprime:
        for yinner in yprime:
            print(0)
            #compare all yprime vals to yprime vals
            #if val < delta
                #deltanew = val
                #ynew = y
                #xnew = ynew's x
            #else if(y-yinner) == delta
                #break out of inner loop
    return xnew,ynew

def calcDist(x,y):
    #return euclidian dist between x and y
    return 0

def compute_closest_points(p,x,y):
    
    #preprocessing
    sorted(x)
    sorted(y)
    xsmall = 0
    ysmall = 0
    delta = 100000000
    
    #base case
    if(len(x) <= 3):
        return brute_force(x,y)
    
    #recursive case
    midIndex = len(x)//2
    Lx = x[:midIndex]
    Rx = x[midIndex:]
    Ly = []
    Ry = []
    midVal = Rx[0]
    for yiter in y:
        if(0):
            return 0
        else:
            return 0
    #Left
    (x1,y1,delta1) = compute_closest_points(p,Lx,Ly)
    #Right
    (x2,y2,delta2) = compute_closest_points(p,Rx,Ry)
    
    #delta = smallest of delta1 and delta2
    #xsmall = correspoinding delta and ysmall = corresponding delta
    
    #Middle
    (x3,y3,delta3) = middle_helper(y,delta,midVal)
    
    if(delta3 <= delta):
        return delta3,x3,y3
    else:
        return delta,xsmall,ysmall

if __name__ == '__main__':
    x = []
    y = []
    p = []
    pair = compute_closest_points(p,x,y)
    print(pair)
