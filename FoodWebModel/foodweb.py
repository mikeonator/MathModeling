# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

import matplotlib.pyplot as plt
from life import treefrog, checkerspot, deermule

def main():
    savedata = world().run(50)
    


class world():
    def __init__(agent):
        agent.time = 0
        agent.timelist = [0]

        #Define variables for the Pacific Treefrog
        agent.treefrogpopulation = 50
        agent.tfroglist = []
        agent.tfrog = treefrog.treefrog(agent.treefrogpopulation, agent.time)

        #Define Variables for Edith's Checkerspot
        agent.checkerpop = 500
        agent.cspotlist = []
        agent.cspot = checkerspot.checkerspot(agent.checkerpop, agent.time)

        #Define Variables for Mule Deer
        agent.deerpop = 350
        agent.mdeerlist = []
        agent.mdeer = deermule.muledeer(agent.deerpop, agent.time)

    def run(agent,final):
        

        for i in range(0, final):
            #Simulate one day of treefrog existence
            agent.tfrog.simulate(agent)
            agent.tfroglist.append(agent.treefrogpopulation)

            #simulate one day of checkerspot existence 
            agent.cspot.simulate(agent)
            agent.cspotlist.append(agent.checkerpop)

            #simulate one day of Mule deer existence
            agent.mdeer.simulate(agent)
            agent.mdeerlist.append(agent.deerpop)

            agent.time +=1
            agent.timelist.append(agent.time)
        
        #combines recorded data into a dictionary, then outputs it
        outdict = {"Time":agent.timelist, "Treefrog":agent.tfroglist, "Checkerspot":agent.cspotlist, "Mule Deer":agent.mdeerlist}
        
        return outdict

if __name__ == '__main__':
    main()