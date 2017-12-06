import numpy
import sys
import helper
import math

def brute_force(x):

    onesmall = x[0]
    twosmall = x[1]
    delta = calcDist(x[0],x[1])#precalc the first
    precalclen = len(x)

    if precalclen == 2:
        return delta,onesmall,twosmall
    
    else:
        for xiter in range(precalclen-1):
            for yiter in range(xiter+1,precalclen):
                dist = calcDist(x[xiter],x[yiter])
                if delta > dist:
                    delta = dist
                    onesmall = x[xiter]
                    twosmall = x[yiter]

    return [delta,onesmall,twosmall]

def middle_helper(delta,y,midpoint):

    bestsofar = delta
    pair1 = []
    pair2 = []
    leny = len(y)

    yprime = [xval for xval in y if (midpoint - delta <= xval[1] <= delta + midpoint)]#all y (whose x val) is within (midpoint+delta,midpoint-delta)

    lenprimey = len(yprime)

    for iterone in range (lenprimey-1):
        for itertwo in range(iterone + 1, min(lenprimey,iterone+7)):
            #compare all yprime vals to yprime vals
            val = calcDist(yprime[iterone],yprime[itertwo])
            if val < delta:
                bestsofar = val
                pair1 = yprime[iterone]
                pair2 = yprime[itertwo]

    return bestsofar,pair1,pair2

def calcDist(x,y):#x is point1 y is point2
    #return numpy.linalg.norm(x - y)
    return math.sqrt((x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)

def compute_closest_points(p,x,y):

    #preprocessing
    minpts = []
    delta = 100000000

    #base case
    if(len(x) <= 3):
        return brute_force(x)

    #recursive case
    midIndex = len(x)//2
    Lx = x[:midIndex]
    Rx = x[midIndex:]
    Ly = []
    Ry = []
    midVal = x[midIndex][1]
    for yiter in y:
        if yiter[1] <= midVal:
            Ly.append(yiter)
        else:
            Ry.append(yiter)

    #Left
    (delta1,x1,y1) = compute_closest_points(p,Lx,Ly)
    #Right
    (delta2,x2,y2) = compute_closest_points(p,Rx,Ry)

    #delta = smallest of delta1 and delta2
    #xsmall = correspoinding delta and ysmall = corresponding delta
    if delta1 > delta2:
        delta = delta2
        minpts = [x2,y2]
    else:
        delta = delta1
        minpts = [x1,y1]


    #Middle
    (delta3,x3,y3) = middle_helper(delta,y,midVal)

    if(delta3 < delta):
        return delta3,x3,y3
    else:
        return delta,minpts[0],minpts[1]

if __name__ == '__main__':
    #need to read in
    x = []
    y = []
    p = numpy.genfromtxt(sys.argv[1])

    import time
    start_time = time.process_time()

    x = sorted(p, key=lambda row: row[1])
    y = sorted(p, key=lambda row: row[2])

    pair = compute_closest_points(p,x,y)

    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))

    returnable = [int(pair[1][0]),int(pair[2][0])]
    helper.write_final_answer(sys.argv[1],returnable)
