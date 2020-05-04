## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree
import matplotlib as mpl
import matplotlib.pyplot as plt

class graphing:        
    def graphone(self,xaxis,yaxis,xlabel,ylabel,ptitle,gtitle,filename):
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
