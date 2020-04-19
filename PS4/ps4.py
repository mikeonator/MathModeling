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




if __name__ == '__main__':
    main()