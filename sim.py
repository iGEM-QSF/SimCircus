from math import *


class Simulation(object):
    """docstring for Simulation"""

    def __init__(self, arg):
        '''
        Ask/define the parameters
        '''
        self.arg = arg
        self.timesteps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.data = {
            "Dummydata": [1, cos(2), 3, 4, 5, 6, 8, 3, 7, 3, 7, 3],
            "dammydata": [cos(x) for x in self.timesteps]
        }
        pass

    def run(self):
        '''
        Start the simulation
        '''
        pass

    def stop(self):
        '''
        stop the simulation
        '''
        pass

    def cycle(self):
        '''
        Iterates through the simultaion steps
        '''
        pass
