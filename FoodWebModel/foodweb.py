# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

from mautils import graphing as mgr
from life.primary import treefrog, checkerspot, deermule

def main():
    days = 100

    savedata = world().run(days)
    
    
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

            agent.time +=1
            agent.timelist.append(agent.time)
        
        #combines recorded data into a dictionary, then outputs it
        outdict = {"Treefrog":agent.tfroglist, "Checkerspot":agent.cspotlist, "Mule Deer":agent.mdeerlist}
        
        return [agent.timelist, outdict]

if __name__ == '__main__':
    main()