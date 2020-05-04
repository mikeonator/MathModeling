import random
class muledeer():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 4/(365*7)
        self.death = 1/(365*6)
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)

        coyote = (((agent.coyotepop)/3) * ((random.randint(0,3)/400)))
        
        lion = (((agent.lionpop)/3) * ((random.randint(0,4)/400)))

        popchange = (reproduction) - (natmortality) - coyote - lion

        self.population += popchange
        
        agent.deerpop = self.population