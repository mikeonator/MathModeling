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

    def yeastalc(self,prop,iyeast,ialc,aprod,atox,carry,deltat):
        ylist = [iyeast]
        alist = [ialc]
        tlist = [0]

        t = 0
        y = iyeast
        a = ialc

        while(y >= 0.01):
            aprime = aprod*y
            yprime = ((prop)*(y)*(1 - (y/carry))) - (atox * (a) * (y))

            deltaa = aprime*deltat
            deltay = yprime*deltat

            t += deltat
            a += deltaa
            y += deltay

            ylist.append(y)
            alist.append(a)
            tlist.append(t)

        print("-"*8)
        print(self.name)
        print("\tFermentation ends when:")
        print("\t\tTime = " + str(tlist[-1]))
        print("\t\tYeast = " + str(ylist[-1]))
        print("\t\tAlcohol = " + str(alist[-1]))
        print("-"*8)
        return {"Alcohol": alist, "Yeast": ylist, "Time" : tlist}

    def yeastalcsugar(self,prop,iyeast,ialc,isug,aprod,atox,stox,scar,deltat):
        ylist = [iyeast]
        alist = [ialc]
        tlist = [0]
        slist = [isug]

        t = 0
        y = iyeast
        a = ialc
        s = isug

        while(y >= 0.01):
            sprime = stox*y
            aprime = aprod*y
            yprime = ((prop)*(y)*(1 - (y/(scar*s)))) - (atox * (a) * (y))

            deltas = sprime*deltat
            deltaa = aprime*deltat
            deltay = yprime*deltat

            s += deltas
            t += deltat
            a += deltaa
            y += deltay

            slist.append(s)
            ylist.append(y)
            alist.append(a)
            tlist.append(t)

        print("-"*8)
        print(self.name)
        print("\tFermentation ends when:")
        print("\t\tTime = " + str(tlist[-1]))
        print("\t\tYeast = " + str(ylist[-1]))
        print("\t\tAlcohol = " + str(alist[-1]))
        print("\t\tSugar = " + str(slist[-1]))
        print("-"*8)
        return {"Alcohol": alist, "Yeast": ylist, "Sugar": slist, "Time" : tlist}

    def maxminCheck(self,check,tlist,test,givenlist = "given list"):
        testval = ""
        ind = ""
        if test == "max":
            ind = check.index(max(check))
            testval = "maximum"
        if test == "min":
            ind = check.index(min(check))
            testval = "minimum"
        print("-"*8)
        print(self.name)
        print("\t\tThe " + testval + " value of the " + givenlist + " is : " + str(check[ind]))
        print("\t\tThis " + testval + " value is reached at time t = " + str(tlist[ind]))
        print("-"*8)

        return [ind]

    def graph(self,xaxis,yaxis,xlabel,ylabel,ptitle,gtitle,filename):
        plt.plot(xaxis,yaxis,label = str(ptitle))
        plt.xlabel(str(xlabel))
        plt.ylabel(str(ylabel))
        plt.title(str(gtitle))
        plt.legend()
        plt.savefig(str(filename))
        plt.close()

    def graphmult(self,ylists,tlist,ylablist,tlabel,gtitle,filename):
        for a in ylists:
            plt.plot(tlist,a,label= ylablist[(ylists.index(a))])
        plt.xlabel(str(tlabel))
        plt.title(str(gtitle))
        plt.legend()
        plt.savefig(str(filename))
        plt.close()
