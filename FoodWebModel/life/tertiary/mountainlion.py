import random

class mountainlion():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.death = 1/(365*12)
        
    def simulate(self,agent):
        
        self.growth = ((random.randint(2,3))/(365*2))

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)

        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.lionpop = self.population