from matplotlib import pyplot as plt
from sim import Simulation


class Visualization(object):
    """docstring for Visualization"""

    def __init__(self, simulation):
        self.simulation = simulation
        self.colors = ['b', 'g', 'c']
        pass

    def visualize(self):
        '''
        Visualizes the current situation
        '''
        for ind, parameter in enumerate(self.simulation.data.keys()):
            print len(self.simulation.timesteps), len(parameter)
            plt.plot(
                self.simulation.timesteps,
                self.simulation.data.get(parameter),
                self.colors[ind])

        plt.xlabel("Time")
        plt.ylabel("Protein concentration")
        plt.legend(self.simulation.data.keys())
        plt.show()

sim = Simulation("asd")
vis = Visualization(sim)
vis.visualize()
