import random

class jackrabbit():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.death = 1/(365*5)
        
    def simulate(self,agent):

        self.growth = ((random.randint(1,4) * (random.randint(3,4))))/(365*12)

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)
        
        coyote = (((agent.coyotepop)/2) * ((random.randint(0,3)/200)))
        
        lion = (((agent.lionpop)/2) * ((random.randint(0,10)/300)))

        popchange = (reproduction) - (natmortality) - (coyote) - (lion)

        self.population += popchange
        
        agent.jackpop = self.population