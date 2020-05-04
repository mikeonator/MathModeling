class treefrog():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 23/365
        self.death = (0.84)/(365)
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)
        
        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.treefrogpopulation = self.population