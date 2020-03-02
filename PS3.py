## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree
import matplotlib as mpl
import matplotlib.pyplot as plt

def sirForFunc(tInitial,tFinal,steps):
        S = 45400.0
        I = 2100.0
        R = 2500.0
        t = tInitial

        sList = [S]
        iList = [I]
        rList = [R]
        tList = [t]

        for a in range(0,steps):

            transCoef = 0.00001

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


def sirWhileFunc(tInitial,tFinal,step):
        S = 45400.0
        I = 2100.0
        R = 2500.0
        t = tInitial

        transCoef = 0.00001

        sPrime = ((-1*transCoef)*(S)*(I))
        iPrime = ((transCoef)*(S)*(I) - (I/14))
        rPrime = (I/14)

        deltaT = ((tFinal - tInitial)/step)

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
        if(iList[-1] < iList[-2]):
            print(t)
            print(I)

        plt.plot(tList, sList, label="S")           # creates piecewise-linear graphs
        plt.plot(tList, iList, label="I")
        plt.plot(tList, rList, label="R")
        plt.plot()

        plt.xlabel("Time (in days) || deltaT: " + str(deltaT))                # sets details for plotting
        plt.ylabel("Number of People")
        plt.title("Measles S-I-R")
        plt.legend()
        plt.savefig('WhileLoopSIR' + str(step) + 'step.png')
        plt.close()



def problemOne():
    print("Problem One\n")
    sirForFunc(0,45,45)
    sirForFunc(0,45,5)
    sirWhileFunc(0,45,1)
    sirWhileFunc(0,45,0.1)
    sirWhileFunc(0,45,0.01)
    sirWhileFunc(0,45,0.001)



def problemTwo():
    print("\nProblem Two\n")
   


def problemThree():
    print("\nProblem Three\n")




def main():
    print("Problem Set 3\n" + 10*"_" + "\n")
    problemOne()
    problemTwo()
    problemThree()


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