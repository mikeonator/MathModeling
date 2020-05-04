import random

class coyote():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.death = 1/(365*12)
        
    def simulate(self,agent):
        
        self.growth = ((random.randint(0,5))/(365*2))

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)

        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.coyotepop = self.population