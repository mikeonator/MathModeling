# Michael Audi - 2020
# Mathematical Modeling :: Mr. Sabree
import matplotlib as mpl
import matplotlib.pyplot as plt

def listCreate():
    tInitial = 10
    tFinal = 100
    iterate = 1000

    step = ((tFinal - tInitial)/iterate)

    S = 45400.0
    I = 2100.0
    R = 2500.0
    t = tInitial

    sList = [S]
    iList = [I]
    rList = [R]
    tList = [t]

    for a in range(tInitial, tFinal, step):
        print(a)
    

    return [sList, iList, rList, tList]


def plotstuff(results):
    print(results)

def main():
    plotstuff(listCreate())

if __name__ == '__main__':
    main()