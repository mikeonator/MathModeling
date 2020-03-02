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
        plt.savefig('ForLoopSIR' + str(steps) + 'step.png')
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
        plt.savefig('WhileLoopSIR' + str(deltaT) + 'delT.png')
        plt.close()

def problemTwo():
    print("\nProblem Two\n")

    print("\ta) " + str(rabbit(100,1000,2000)[1][36]).split(".")[0] + "." + str(rabbit(100,1000,2000)[1][36]).split(".")[1][0:2])

    print("\tb) The carrying capacity of the logistic equation is 2000")

    plt.plot(rabbit(100,100,2000)[0],rabbit(100,100,2000)[1], label="100")
    plt.plot(rabbit(2000,100,2000)[0],rabbit(2000,100,2000)[1], label="2000")
    plt.plot(rabbit(2500,100,2000)[0],rabbit(2500,100,2000)[1], label="2500")
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of Rabbits")
    plt.title("Rabbit Population Growth varied on starting value")
    plt.legend()
    plt.savefig("rabbitPopGrowthStart.png")
    plt.close()
    print("\tc) Done.")


    plt.plot(rabbit(100,150,1000)[0],rabbit(100,150,1000)[1], label="1000")
    plt.plot(rabbit(100,150,3000)[0],rabbit(100,150,3000)[1], label="3000")
    plt.plot(rabbit(100,150,500)[0],rabbit(100,150,500)[1], label="500")
    plt.plot(rabbit(100,150,4500)[0],rabbit(100,150,4500)[1], label="4500")
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of Rabbits")
    plt.title("Rabbit Population Growth varied on Carrying Capacity")
    plt.legend()
    plt.savefig("rabbitPopGrowthCarry.png")
    plt.close()


def rabbit(rZero,tFinal,carry):
    R = rZero
    rabbitList = [[],[]]
    
    for a in range(0,tFinal+1):
        #print("t = " + str(a + 1) + " ||| r = " + str(R))
        rPrime = ((0.1)*R*(1-(R/carry)))
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








#     import matplotlib as mpl                    # imports necessary libraries and
# mpl.use('Agg')                              # packages
# import matplotlib.pyplot as plt

# tinitial = 0                                # sets iniial and final time values
# tfinal = 80.0

# t = tinitial                                # sets the intial values for t, S,
# S = 45400.0                                 # I, and R
# I = 2100.0
# R = 2500.0

# tlist = [t]                                 # creates lists for t, S, I, and R
# Slist = [S]
# Ilist = [I]
# Rlist = [R]

# numberofsteps = 1000                        # sets the number of timesteps

# deltat = (tfinal - tinitial)/numberofsteps  # calculates the length of steps

# for k in range(1,numberofsteps + 1):        # begins the loop

#     Sprime = -0.00001 * S * I               # calculates the current rates of
#     Iprime = (0.00001 * S * I) - (I / 14.0) # change
#     Rprime = I / 14.0

#     deltaS = Sprime * deltat                # calculates the current change
#     deltaI = Iprime * deltat
#     deltaR = Rprime * deltat

#     t = t + deltat                          # updates the current time

#     S = S + deltaS                          # updates the current values
#     I = I + deltaI
#     R = R + deltaR

#     tlist.append(t)                         # adds current values to lists
#     Slist.append(S)
#     Ilist.append(I)
#     Rlist.append(R)

# plt.plot(tlist, Slist, label="S")           # creates piecewise-linear graphs
# plt.plot(tlist, Ilist, label="I")
# plt.plot(tlist, Rlist, label="R")
# plt.plot()

# plt.xlabel("Time (in days)")                # sets details for plotting
# plt.ylabel("Number of People")
# plt.title("Measles S-I-R")
# plt.legend()
# plt.show()

# plt.savefig('sir.png')