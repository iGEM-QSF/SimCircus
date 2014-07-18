from math import *


class Simulation(object):
    """docstring for Simulation"""

    def __init__(self, arg):
        '''
        Ask/define the parameters
        '''
        self.arg = arg
        self.YF1 = 0
        self.PYF1 = 0
        self.FixJ = 0
        self.PFixJ = 0
        self.CI = 0
        self.TetR = 0 
        self.A = 
        self.B = 
        self.C = 
        self.P1 = 
        self.P2 = 
        self.P3 = 
        self.P4 = 
        self.P5 = 
        self.RBS1 = 
        self.RBS2 = 
        self.step = 
        self.MaxTime =   
        self.AllData = {}

        self.timesteps = 
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
