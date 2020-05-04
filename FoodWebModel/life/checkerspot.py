class checkerspot():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 250/(365*24)
        self.death = 10/(365)
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)
        
        popchange = (reproduction) - (natmortality)

        self.population += popchange
        
        agent.checkerpop = self.population