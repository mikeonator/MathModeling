class muledeer():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 3
        self.death =3
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)
        
        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.treefrogpopulation = self.population