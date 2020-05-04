import random

class whiptail():
    def __init__(self, population, time):
        self.population = population
        self.time = time

        self.growth = 5/365
        self.death = 1/(365*3)
        
    def simulate(self,agent):

        reproduction = (self.population * self.growth)

        natmortality = (self.population * self.death)

        coyote = (((agent.coyotepop)/3) * ((random.randint(0,10)/300)))

        lion = (((agent.lionpop)/3) * ((random.randint(0,10)/300)))

        carry = (1-(agent.whipop/200))
        print("carry " + str(carry) + "|| pop " + str(agent.whipop) + " || Time = " + str(agent.time))

        popchange = (((reproduction) - (natmortality))*carry) - (coyote) - (lion)

        self.population += popchange
        
        agent.whipop = self.population