import matplotlib as mpl
import matplotlib.pyplot as plt


class goodfunc:
    def __init__(self,name):
        self.name = name

    def cooling(self,prop,initial,final,room,step):
        xlist = [initial]
        tlist = [0]
        t = 0
        x = initial
        deltat = 0
        if (initial < final):
            deltat = (final - initial)/step
        if (initial > final):
            deltat = (initial - final)/step
        while(((initial > final)and (x >= final)) or ((initial < final) and (x <= final))):
            xprime = (prop)*(x - room)
            deltax = (deltat * xprime)
            t += deltat
            x += deltax
            xlist.append(x)
            tlist.append(t)
        return [xlist,tlist]

    def yeastnoalc(self,prop,initial,carry,time,step):
        xlist = [initial]
        tlist = [0]
        t = 0
        x = initial
        deltat = (time)/step
        half = 0

        while(x <= (0.99*carry)):
            xprime = (prop)*(x)*(1-(x/carry))
            deltax = (deltat * xprime)
            t += deltat
            x += deltax
            xlist.append(x)
            tlist.append(t)
            if (x >= ((carry/2) - 0.1) and (x <= ((carry/2) + 0.1))):
                half = t
        print("-"*8)
        print(self.name)
        print("\t\tThe yeast reaches 1% of the carrying capacity at time :: " + str(tlist[-1]))
        if not(half == 0):
            print("\t\tThe yeast reaches 50% of the carrying capacity at time :: " + str(half))
        print("-"*8)

        return [xlist,tlist]

    def graph(self,xaxis,yaxis,xlabel,ylabel,ptitle,gtitle,filename):
        plt.plot(xaxis,yaxis,label = str(ptitle))
        plt.xlabel(str(xlabel))
        plt.ylabel(str(ylabel))
        plt.title(str(gtitle))
        plt.legend()
        plt.savefig(str(filename))
        plt.close()