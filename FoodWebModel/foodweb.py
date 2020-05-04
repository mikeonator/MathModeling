# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

import tools
from life import test, treefrog

def main():
    wrld = world()
    wrld.run(11)


class world():
    def __init__(agent):
        agent.time = 0

        #Define variables for the Pacific Treefrog
        agent.treefrogpopulation = 50
        agent.tfrog = treefrog.treefrog(agent.treefrogpopulation, agent.time)


    def run(agent,final):

        for i in range(0,final):
            agent.tfrog.simulate(agent)
            print(agent.treefrogpopulation)
            
            
            
            
            
            
            
            agent.time +=1

if __name__ == '__main__':
    main()