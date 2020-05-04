# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

import matplotlib.pyplot as plt
from life import test, treefrog, checkerspot, deermule

def main():
    final = 50

    wrld = world()
    for i in range(0, final):
        wrld.run()


class world():
    def __init__(agent):
        agent.time = 0

        #Define variables for the Pacific Treefrog
        agent.treefrogpopulation = 50
        agent.tfrog = treefrog.treefrog(agent.treefrogpopulation, agent.time)

        #Define Variables for Edith's Checkerspot
        agent.checkerpop = 500
        agent.cspot = checkerspot.checkerspot(agent.checkerpop, agent.time)

        #Define Variables for Mule Deer
        agent.deerpop = 350
        agent.mdeer = deermule.muledeer(agent.deerpop, agent.time)

    def run(agent):

        #Simulate one day of treefrog existence
        agent.tfrog.simulate(agent)
        #print(agent.treefrogpopulation)

        #simulate one day of checkerspot existence 
        agent.cspot.simulate(agent)
        #print(agent.checkerpop)

        #simulate one day of Mule deer existence
        agent.mdeer.simulate(agent)
        #print(agent.deerpop)

            
        agent.time +=1

if __name__ == '__main__':
    main()