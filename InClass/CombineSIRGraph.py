# Michael Audi - Collegiate School Class of 2020
## Math Modeling
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def sirForFunc(tInitial,tFinal,deltaT):
        S = 45400.0
        I = 2100.0
        R = 2500.0
        t = tInitial

        sList = [S]
        iList = [I]
        rList = [R]
        tList = [t]

        numberofsteps = math.ceil((tFinal - tInitial)/(deltaT))


        for a in range(0,numberofsteps+1):

            transCoef = 0.00001

            sPrime = ((-1*transCoef)*(S)*(I))
            iPrime = ((transCoef)*(S)*(I) - (I/14))
            rPrime = (I/14)

            deltaS = (sPrime*deltaT)
            deltaI = (iPrime*deltaT)
            deltaR = (rPrime*deltaT)

            S += deltaS
            I += deltaI
            R += deltaR
            t += deltaT

            sList.append(S)
            iList.append(I)
            rList.append(R)
            tList.append(t)

        plt.plot(tList, sList, label=("S"+str(deltaT)))           # creates piecewise-linear graphs
        plt.plot()
        #print("\n\tsList")
        #print(sList)
        #print("\n\tiList")
        #print(iList)
        #print("\n\trList")
        #print(rList)
        #print("\n\ttList")
        #print(tList)


def main():
    for a in range(1,7):
        sirForFunc(0,40,a)
  
    plt.xlabel("Time (in days) with varying deltaT's")                 # sets details for plotting
    plt.ylabel("Number of People")
    plt.title("Measles S")
    plt.legend()
    plt.savefig("InClass/SIRDeltaTDiff.png")
    plt.close()





if __name__ == '__main__':
    main()