import random
import threading
from visualize import Visualization


class FakeSimulation(threading.Thread):

    def __init__(self):
        #Threading actions, non threaded example may be feasible
        #now that a new visualization version was made.
        threading.Thread.__init__(self)
        self.data = {
            "Parameter 1": [],
            "Parameter 2": []
        }
        self.timesteps = []
        self.ib = 0.0
        self.vis = Visualization(self)
        self.vis.start()

    def run(self):
        for i in range(100):
            print self.ib
            self.data["Parameter 1"].append(random.randint(1, 15))
            self.data["Parameter 2"].append(random.randint(1, 15))
            self.timesteps.append(i)
            self.vis.update()


sim = FakeSimulation()
sim.start()
