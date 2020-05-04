class muledeer():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 4/(365*14)
        self.death = 1/(365*6)
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)
        
        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.deerpop = self.population