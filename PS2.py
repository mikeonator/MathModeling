# Michael Audi - Collegiate School Class of 2020
## Math Modeling Problem Set Two Answers
import matplotlib.pyplot as plt


def problemOne():
    print("Problem One\n")

    print("a)   12 to 13 days      and      13,000 people")
    print("b)   Initial: 42,000 people     and     16 days")
    print("c)   About 33 days to reach 25000 recovered and eventually everyone recovers")
    print("d)   Max Increase: ~5 days     and     Max Decrease: ~16 days")
    print("e)   Area under the curve from t = range(1,21)     << (t=1-20)\n     or also doable with (R@t=20 + I@t=20)\n")



def problemTwo():
    print("\nProblem Two\n")
    # \/ initial values \/
    S = 44000
    I = 500
    R = 0
    print("S=" + str(S))
    print("I=" + str(I))
    print("R=" + str(R))

    transCoef = 0.00001
    sPrime = ((-1*transCoef)*(S)*(I))
    iPrime = ((transCoef)*(S)*(I) - (I/14))
    rPrime = (I/14)

    timemax = 25

    for a in range(0,(timemax+1)):
        newS = S
        newI = I
        newR = R

        deltaS = newS+(sPrime*a)
        deltaI = newI+(iPrime*a)
        deltaR = newR+(rPrime*a)

        print("time = " + str(a))                                                               # Print current t value
        print("\tS = " + str(deltaS) + "\n\tI = " + str(deltaI) + "\n\tR = " + str(deltaR))     # Print S, I, and R for value t=a
        print(5*"_" + "\n")                                                                     # Print a line

        S = newS
        I = newI
        R = newR


def problemThree():
    print("\nProblem Three\n")



def main():
    print("Problem Set 2\n" + 10*"_" + "\n")
    problemOne()
    problemTwo()
    problemThree()






if __name__ == '__main__':
    main()