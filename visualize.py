#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
#from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2TkAgg

#from matplotlib import pyplot as plt
import random
from matplotlib.figure import Figure

import threading
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


class Visualization(object):
    """docstring for Visualization"""

    def __init__(self, simulation):
        #Initialize drawing parameters
        self.simulation = simulation
        self.legend = simulation.data.keys()
        self.toggle_list = [1 for i in simulation.data.keys()]
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def start(self):

        #Tkinter related actions
        self.root = Tk.Tk()
        self.root.wm_title("SimCircus by Aalto-Helsinki")

        button = Tk.Button(master=self.root, text='Quit', command=self._quit)
        button.pack(side=Tk.BOTTOM)
        b = Tk.Button(master=self.root, text='Run', command=self.simulation.run)
        b.pack(side=Tk.BOTTOM)

        self.button_frame = Tk.Frame(self.root)

        buttons = []

        for ind, parameter in enumerate(self.simulation.data.keys()):
            temp = Tk.Button(
                master=self.button_frame,
                text=parameter + str(ind),
                command=lambda ind=ind: self.toggle(ind))
            temp.pack(side=Tk.TOP)
            buttons.append(temp)

        self.button_frame.pack(side=Tk.RIGHT)

        self.figure = Figure(figsize=(10, 8), dpi=100)

        # tk.DrawingArea
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


class FakeSimulation(threading.Thread):

    def __init__(self):
        #Threading actions
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
#vis.visualize()


# implement the default mpl key bindings
#from matplotlib.backend_bases import key_press_handler


'''
def on_key_event(event):
    print('you pressed %s' % event.key)
    #key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)
'''


# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
