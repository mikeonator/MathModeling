## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import e
from savefunc import goodfunc

def main():
    problemOne()
    problemTwo()


def problemOne():
    print()
    oned = goodfunc("1d").cooling((-9/110),180,120,70,1000000)
    goodfunc("1e").graph(oned[1],oned[0],"Time in min","Temperature in Fahrenheit","temp/time","A Graph of Temp (in F) over time (in min) of a Coffee cup in a room @70 deg F","PS4/coffeegraph.png")

def problemTwo():
    twob = goodfunc("2b").yeastnoalc((2/9),0.5,10,50,1000)
    goodfunc("2b").graph(twob[1],twob[0],"Time in hours","Yeast in lbs","yeast/time","Pounds of Yeast per Time in hours with k = (2/9)","PS4/yeast/yeasttwob.png")

    twoc = goodfunc("2c").yeastnoalc((1/9),0.5,10,50,1000)
    goodfunc("2c").graph(twoc[1],twoc[0],"Time in hours","Yeast in lbs","yeast/time","Pounds of Yeast per Time in hours with k = (1/9)","PS4/yeast/yeasttwoc.png")

    twof = goodfunc("2f").yeastalc((2/9), 0.5, 0, 0.05, 0.1, 10, 0.01)
    goodfunc("2f").graphmult([twof["Alcohol"],twof["Yeast"]],twof["Time"],["Alcohol","Yeast"],"Time in hours","Yeast and Alcohol Content over time","PS4/yeast/yeastalctwof.png")
    goodfunc("2f").maxminCheck(twof["Yeast"],twof["Time"],'max',"yeast list")

    twog1 = goodfunc("2g1").yeastalc((2/9), 0.5, 0, 0.25, 0.02, 10, 0.01)
    goodfunc("2g1").graphmult([twog1["Alcohol"],twog1["Yeast"]],twog1["Time"],["Alcohol","Yeast"],"Time in hours","Yeast and Alcohol Content over time","PS4/yeast/yeastalctwog1.png")

    twog2 = goodfunc("2g2").yeastalc((2/9), 0.5, 0, 0.25, 0.1, 10, 0.01)
    goodfunc("2g2").graphmult([twog2["Alcohol"],twog2["Yeast"]],twog2["Time"],["Alcohol","Yeast"],"Time in hours","Yeast and Alcohol Content over time","PS4/yeast/yeastalctwog2.png")

    twog3 = goodfunc("2g3").yeastalc((2/9), 0.5, 0, 0.05, 0.02, 10, 0.01)
    goodfunc("2g3").graphmult([twog3["Alcohol"],twog3["Yeast"]],twog3["Time"],["Alcohol","Yeast"],"Time in hours","Yeast and Alcohol Content over time","PS4/yeast/yeastalctwog3.png")

    twoj = goodfunc("2j").yeastalcsugar((2/9), 0.5, 0, 25, 0.05, 0.1, -0.15, 0.4, 0.01)
    goodfunc("2j").graphmult([twoj["Alcohol"],twoj["Yeast"],twoj["Sugar"]],twoj["Time"],["Alcohol","Yeast","Sugar"],"Time in hours","Yeast, Alcohol, and Sugar Content over time","PS4/yeast/yeastalcsugartwoj.png")

if __name__ == '__main__':
    main()