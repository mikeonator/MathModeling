import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    coronaModel(0.000000032725289,50)

def coronaModel(a,b):
    
    S = 19540000
    I = 1
    R = 0
    t = 0

    sList = [S]
    iList = [I]
    rList = [R]
    tList = [t]

    while (I >= 1):
        sPrime = (-1*a*S*I)
        iPrime = ((a*S*I) - (I/b))
        rPrime = (I/b)

        deltaT = 0.001
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
    print("Time :: " + str(t) + " || I :: " + str(I))
    print("Number of Iterations :: " + str(len(tList)))

    plt.plot(tList, sList, label=("S" + str(deltaT)))           # creates piecewise-linear graphs
    plt.plot(tList, iList, label=("I" + str(deltaT)))
    plt.plot(tList, rList, label=("R" + str(deltaT)))
    plt.xlabel("Time (in days) until I <= 1 (with deltaT = " + str(deltaT) + ")")                 # sets details for plotting
    plt.ylabel("Number of People")
    plt.title("Time :: " + str(t) + "\nI :: " + str(I) + "\nNumber of Iterations :: " + str(len(tList)))
    plt.legend(loc="best")
    plt.savefig("InClass/Corona Model/CoronaSIRGraph.png")
    plt.close()






if __name__ == '__main__':
    main()