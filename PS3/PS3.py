## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree
import matplotlib as mpl
import matplotlib.pyplot as plt

def problemOne():
    print("Problem One\n")
    print("\ta)\nDone.")
    sirForFunc(0,45,45)
    sirForFunc(0,45,5)
    print("\tb)  The value of I' is going to be negative")

    print("\tc)  I mean I kinda just did it it's a bit hard to describe")

    print("\td)")
    sirWhileFunc(0,45,1)
    print("\te)")
    sirWhileFunc(0,45,0.1)
    print("\tf)")
    sirWhileFunc(0,45,0.01)
    print("\tg)")
    sirWhileFunc(0,45,0.001)

def sirForFunc(tInitial,tFinal,steps):
        S = 45400.0
        I = 2100.0
        R = 2500.0
        t = tInitial
        x = 1

        sList = [S]
        iList = [I]
        rList = [R]
        tList = [t]

        for a in range(0,steps):

            transCoef = 0.00001

            if((a > 1) and (iList[-1] < iList[-2]) and (x == 1)):
                print("\t\tT :: " + str(t))
                print("\t\tI' :: " + str(iPrime))
                print("\t\t"+ "_"*4)
                x = 0

            sPrime = ((-1*transCoef)*(S)*(I))
            iPrime = ((transCoef)*(S)*(I) - (I/14))
            rPrime = (I/14)
            deltaT = ((tFinal - tInitial)/steps)

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

        plt.plot(tList, sList, label="S")           # creates piecewise-linear graphs
        plt.plot(tList, iList, label="I")
        plt.plot(tList, rList, label="R")
        plt.plot()

        plt.xlabel("Time (in days) || Step: " + str(steps))                # sets details for plotting
        plt.ylabel("Number of People")
        plt.title("Measles S-I-R")
        plt.legend()
        plt.savefig('PS3/ForLoopSIR' + str(steps) + 'step.png')
        plt.close()

def sirWhileFunc(tInitial,tFinal,deltaT):
        S = 45400.0
        I = 2100.0
        R = 2500.0
        t = tInitial

        transCoef = 0.00001

        sPrime = ((-1*transCoef)*(S)*(I))
        iPrime = ((transCoef)*(S)*(I) - (I/14))
        rPrime = (I/14)

        sList = [S]
        iList = [I]
        rList = [R]
        tList = [t]

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

        while(iList[-1] > iList[-2]):
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

        if((len(tList) > 2) and(iList[-1] < iList[-2])):
            print("\t\tT :: " + str(t - deltaT))
            print("\t\tI :: " + str(I - deltaI))
            print("\t\t" + "_"*4)

        plt.plot(tList, sList, label="S")           # creates piecewise-linear graphs
        plt.plot(tList, iList, label="I")
        plt.plot(tList, rList, label="R")
        plt.plot()

        plt.xlabel("Time (in days) || deltaT: " + str(deltaT))                # sets details for plotting
        plt.ylabel("Number of People")
        plt.title("Measles S-I-R")
        plt.legend()
        plt.savefig('PS3/WhileLoopSIR' + str(deltaT) + 'delT.png')
        plt.close()

def problemTwo():
    print("\nProblem Two\n")

    print("\ta) " + str(rabbit(100,1000,0.1,2000)[1][36]).split(".")[0] + "." + str(rabbit(100,1000,0.1,2000)[1][36]).split(".")[1][0:2])

    print("\tb) The carrying capacity of the logistic equation is 2000")

    plt.plot(rabbit(100,100,0.1,2000)[0],rabbit(100,100,0.1,2000)[1], label="100")
    plt.plot(rabbit(2000,100,0.1,2000)[0],rabbit(2000,100,0.1,2000)[1], label="2000")
    plt.plot(rabbit(2500,100,0.1,2000)[0],rabbit(2500,100,0.1,2000)[1], label="2500")
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of Rabbits")
    plt.title("Rabbit Population Growth varied on starting value")
    plt.legend()
    plt.savefig("PS3/rabbitPopGrowthStart.png")
    plt.close()
    print("\tc) Done.")

    plt.plot(rabbit(100,150,0.1,1000)[0],rabbit(100,150,0.1,1000)[1], label="1000")
    plt.plot(rabbit(100,150,0.1,3000)[0],rabbit(100,150,0.1,3000)[1], label="3000")
    plt.plot(rabbit(100,150,0.1,500)[0],rabbit(100,150,0.1,500)[1], label="500")
    plt.plot(rabbit(100,150,0.1,4500)[0],rabbit(100,150,0.1,4500)[1], label="4500")
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of Rabbits")
    plt.title("Rabbit Population Growth varied on Carrying Capacity")
    plt.legend()
    plt.savefig("PS3/rabbitPopGrowthCarry.png")
    plt.close()
    print("\td) They all have the same shape, just approach a greater asymptote")

    plt.plot(rabbit(100,150,-0.1,2000)[0],rabbit(100,150,-0.1,2000)[1], label="-0.1")
    plt.plot(rabbit(100,150,0.1,2000)[0],rabbit(100,150,0.1,2000)[1], label="0.1")
    plt.plot(rabbit(100,150,2,2000)[0],rabbit(100,150,2,2000)[1], label="2")
    plt.plot(rabbit(100,150,-2,2000)[0],rabbit(100,150,-2,2000)[1], label="-2")
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of Rabbits")
    plt.title("Rabbit Population Growth varied on k value")
    plt.legend()
    plt.savefig("PS3/rabbitPopGrowthModifier.png")
    plt.close()
    print("\te) As the K value gets larger, the function instead oscillates around the carrying capacity with a larger amplitude. I'm not exactly sure what making it negative is doing to the function")

    print("\tf) ")



def rabbit(rZero,tFinal,K,L):
    R = rZero
    rabbitList = [[],[]]
    
    for a in range(0,tFinal+1):
        #print("t = " + str(a + 1) + " ||| r = " + str(R))
        rPrime = ((K)*R*(1-(R/L)))
        R += rPrime
        rabbitList[0].append(a)
        rabbitList[1].append(R)
    return rabbitList 


def main():
    print("Problem Set 3\n" + 10*"_" + "\n")
    problemOne()
    problemTwo()


if __name__ == '__main__':
    main()