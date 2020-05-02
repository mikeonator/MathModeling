

class testanimal():
    def __init__(self, population, time):
        print("presim")
        self.population = population
        self.time = time
        print(self.population, self.time)
        print("x"*5)
    def simulate(self,agent):
        self.population = agent.population
        self.time = agent.time
        print("postsim")
        print(self.population, self.time)
        print("="*8)
