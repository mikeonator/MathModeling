# Michael Audi - Collegiate School Class of 2020
## Math Modeling

from decimal import Decimal
import matplotlib.pyplot as plt

def main():
    x = 0
    y = 3
    #print("[ " + str(x) + " ] | [ " + str(y) + " ]")
    #print("___________" + "_"*(len(str(x))) + "_"*(len(str(y))))
    deltax = 0.001
    
    start = 1
    end = 10000
    
    xlist = [x]
    ylist = [y]
    steplist = []
    
    for k in range(start, (end+1)):
        yprime = (2*x*y) - (3*(y**2)) + (2*x)
        
        deltay = yprime*deltax

        y = y + deltay
        x = x + deltax

        steplist.append(k)
        xlist.append(x)
        ylist.append(y)

        
        #scinotx = x     #'%.2E' % Decimal(str(x))
        #scinoty = y     #'%.2E' % Decimal(str(y))

        #print("[ " + str(scinotx) + " ] | [ " + str(scinoty) + " ]")
        #print("="*7 + "="*(len(str(scinotx))) + "="*(len(str(scinoty))))

    biglist = [steplist, xlist, ylist]

    for a in range(0, len(steplist)):
        print(str(biglist[0][a]) + " ][ " + str(biglist[1][a]) + " ][ " + str(biglist[2][a]))

if __name__ == '__main__':
    main()