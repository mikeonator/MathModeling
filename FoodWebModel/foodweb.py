# - Alejandro Astudillo and Michael Audi
# - Mr. Sabree
# - Mathematical Modeling 2020
# - Collegiate School

import tools
import life.test as test

def main():
    wrld = world()
    wrld.run()


class world():
    def run(agent):
        agent.population = 0
        agent.time = 0
        testy = test.testanimal(agent.population, agent.time)
        for a in range(0,11):
            agent.population += 1
            agent.time += 1
            testy.simulate(agent)

if __name__ == '__main__':
    main()