import matplotlib as mpl
import matplotlib.pyplot as plt



def main():
    coefList = [0.111,0.098,0.002,0.01]
    coronaModel(coefList[0],coefList[1],coefList[2],coefList[3])


def coronaModel(a,b,c,d):
    
    S = 8398748
    I = 1
    R = 0
    D = 0
    t = 0

    sList = [S]
    iList = [I]
    rList = [R]
    dList = [D]
    tList = [t]

    while (I >= 0):
        sPrime = (-1)*(a)*(S)*(I) + (d*R)
        iPrime = (a)*(S)*(I) - (b*I) - (c*I)
        rPrime = (b*I) - (d*R)
        dPrime = (c*I)

        deltaT = 0.1
        deltaS = (sPrime*deltaT)
        deltaI = (iPrime*deltaT)
        deltaR = (rPrime*deltaT)
        deltaD = (dPrime*deltaT)

        S += deltaS
        I += deltaI
        R += deltaR
        D += deltaD
        t += deltaT

        sList.append(S)
        iList.append(I)
        rList.append(R)
        dList.append(D)
        tList.append(t)
    
    print(iList)
    







if __name__ == '__main__':
    main()