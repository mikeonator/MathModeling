import random

class treefrog():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.death = (55)/(365*6)
        
    def simulate(self,agent):
        
        self.growth = ((random.randint(400,750)*0.04)/(365*2))

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)

        whiptail = ((random.randint(0,3)/400))*((agent.whipop)/2)

        carry = (1-(agent.tfrogpop/300))

        popchange = (((reproduction) - (natmortality))) - (whiptail)

        self.population += (popchange)
        
        agent.tfrogpop = self.population