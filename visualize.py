#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
#from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2TkAgg

#from matplotlib import pyplot as plt
from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


class Visualization(object):
    """
    Visualization is a class for visualizing any kind of time series data in
    real time.

    @requires:
    simulation, object
        @attrs
        simulation.data, dictionary
            Includes all the parameter names as keys and the time series
            (list of values) as the values
        simulation.timesteps
            List of timesteps (float or integer),
            same dimension as every paramter
        simulation.ib, float
            Blue light intensity parameter with value between 0.0 and 1.0

    start()
        Initializes the GUI, required to visualize the simulation

    update()
        Updates the data in the graph
        start() has to be run before calling this function

    Example 1:
        vis = Visualization(simulation)
        vis.start()
        for i in range(1000):
            simulation.iteration()
            vis.update()

    The previous example updates the simulation data in each timestep

    Example 2:
        import random
        import threading
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
                self.vis = Visualization(self)
                self.vis.start()

            def run(self):
                for i in range(100):
                    print i
                    self.data["Parameter 1"].append(random.randint(1, 15))
                    self.data["Parameter 2"].append(random.randint(1, 15))
                    self.timesteps.append(i)
                    self.vis.update()


        sim = FakeSimulation()
        sim.start() #May not be necessary

    The example 2 is a ready copy-and-paste demonstration of how this works.
    """

    def __init__(self, simulation):
        #Initialize drawing parameters
        self.simulation = simulation
        self.legend = simulation.data.keys()
        self.toggle_list = [1 for i in simulation.data.keys()]
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'b:']

    def start(self):

        #Tkinter related actions
        self.root = Tk.Tk()
        self.root.wm_title('SimCircusVisualizer 3000 Ultra+ by Aalto-Helsinki')

        button = Tk.Button(master=self.root, text='Quit', command=self._quit)
        button.pack(side=Tk.BOTTOM)

        # Creating the right sidebar
        self.button_frame = Tk.Frame(self.root)

        buttons = []

        for ind, parameter in enumerate(self.simulation.data.keys()):
            temp = Tk.Button(
                master=self.button_frame,
                text=parameter,
                command=lambda ind=ind: self.toggle(ind))
            temp.pack(side=Tk.TOP)
            buttons.append(temp)

        self.intensity = Tk.DoubleVar()
        scale = Tk.Scale(
            self.button_frame,
            variable=self.intensity,
            label="Light intensity",
            from_=0.0,
            to=1.0,
            resolution=0.01,
            command=self.set_intensity)
        scale.pack(side=Tk.BOTTOM)

        self.button_frame.pack(side=Tk.RIGHT)

        # DrawingArea
        self.figure = Figure(figsize=(10, 8), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.root)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.root.after(0, self.simulation.start)

        self.root.mainloop()

    def update(self):
        '''
        Visualizes the current situation
        '''
        active_legend = [legend for ind, legend in enumerate(self.legend)
                         if self.toggle_list[ind]]
        self.figure.clf()

        a = self.figure.add_subplot(
            111,
            xlabel="Time",
            ylabel="Protein concentration")

        for ind, parameter in enumerate(self.simulation.data.keys()):
            if self.toggle_list[ind]:
                a.plot(
                    self.simulation.timesteps,
                    self.simulation.data.get(parameter),
                    self.colors[ind])

        a.legend(active_legend, "upper right")
        self.canvas.show()
        self.toolbar.update()

    def set_intensity(self, current_value):
        self.simulation.ib = current_value

    def toggle(self, ind):
        if self.toggle_list[ind]:
            self.toggle_list[ind] = 0
        else:
            self.toggle_list[ind] = 1
        self.update()

    def _quit(self):
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
