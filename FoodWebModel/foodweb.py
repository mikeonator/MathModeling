# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

from mautils import graphing as mgr
from life.primary import treefrog, checkerspot, deermule
from life.secondary import jackrabbit, whiptail
from life.tertiary import coyote, mountainlion

def main():
    days = int(365)

    savedata = world().run(days)
    #print(savedata[1]["Whiptail"])
    #graphing stuff
    ylablist = list(savedata[1].keys())
    ylist = []
    for a in ylablist:
        ylist.append(savedata[1][a])
    mgr.graphmult("graph", ylist, savedata[0], ylablist, "Time (in days)", ("Food Web population values over " + str(days) + " days."), "FoodWebModel/foodweb.png")



class world():
    def __init__(agent):
        agent.time = 0
        agent.timelist = [0]

        #Define variables for the Pacific Treefrog
        agent.tfrogpop = 50
        agent.tfroglist = [agent.tfrogpop]
        agent.tfrog = treefrog.treefrog(agent.tfrogpop, agent.time)

        #Define Variables for Edith's Checkerspot
        agent.checkerpop = 500
        agent.cspotlist = [agent.checkerpop]
        agent.cspot = checkerspot.checkerspot(agent.checkerpop, agent.time)

        #Define Variables for Mule Deer
        agent.deerpop = 350
        agent.mdeerlist = [agent.deerpop]
        agent.mdeer = deermule.muledeer(agent.deerpop, agent.time)

        #Define variables for Jackrabbit
        agent.jackpop = 500
        agent.jackpoplist = [agent.jackpop]
        agent.jackrab = jackrabbit.jackrabbit(agent.jackpop, agent.time)
        
        #define variables for whiptail
        agent.whipop = 50
        agent.whipoplist = [agent.whipop]
        agent.whiptail = whiptail.whiptail(agent.whipop, agent.time)

        #define variables for coyote
        agent.coyotepop = 24
        agent.coyotepoplist = [agent.coyotepop]
        agent.coyote = coyote.coyote(agent.coyotepop, agent.time)

        #define variables for mountain lion
        agent.lionpop = 30
        agent.lionpoplist = [agent.lionpop]
        agent.lion = mountainlion.mountainlion(agent.lionpop, agent.time)


    def run(agent,final):
        

        for i in range(0, final):
            #Simulate one day of treefrog existence
            agent.tfrog.simulate(agent)
            agent.tfroglist.append(agent.tfrogpop)

            #simulate one day of checkerspot existence 
            agent.cspot.simulate(agent)
            agent.cspotlist.append(agent.checkerpop)

            #simulate one day of Mule deer existence
            agent.mdeer.simulate(agent)
            agent.mdeerlist.append(agent.deerpop)

            #simulate one day of jackrabbit existence
            agent.jackrab.simulate(agent)
            agent.jackpoplist.append(agent.jackpop)

            #simulate one day of Western Whiptail existence
            agent.whiptail.simulate(agent)
            agent.whipoplist.append(agent.whipop)

            #simulate one day of coyote existence
            agent.coyote.simulate(agent)
            agent.coyotepoplist.append(agent.coyotepop)

            #simulate one day of lion existence
            agent.lion.simulate(agent)
            agent.lionpoplist.append(agent.lionpop)

            agent.time +=1
            agent.timelist.append(agent.time)
        
        #combines recorded data into a dictionary, then outputs it
        outdict = {"Treefrog":agent.tfroglist, "Checkerspot":agent.cspotlist, "Mule Deer":agent.mdeerlist, "Jackrabbit":agent.jackpoplist, "Whiptail":agent.whipoplist, "Coyote":agent.coyotepoplist, "Mountain Lion":agent.lionpoplist}
        
        return [agent.timelist, outdict]

if __name__ == '__main__':
    main()