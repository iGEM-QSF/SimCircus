from math import *
from visualize import Visualization

import threading


class Simulation(threading.Thread):
    """docstring for Simulation"""

    def __init__(self):
        threading.Thread.__init__(self)
        '''
        Ask/define the parameters
        '''
        self.yf1 = 0
        self.pyf1 = 0
        self.fixj = 0
        self.pfixj = 0
        self.ci = 0
        self.tetr = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.promotor1 = 1
        self.promotor2 = 0
        self.promotor3 = 1
        self.promotor4 = 0
        self.promotor5 = 0
        self.rbs1 = 1
        self.rbs2 = 0.75
        self.dePhosCoeff1 = 0.5
        self.dePhosCoeff2 = 0.5
        self.phosp = 1
        self.ib = 0
        self.degCoeffYF1 = 1
        self.degCoeffFixJ = 1
        self.degCoeffCI = 1
        self.degCoeffTetR = 1
        self.degCoeffA = 0.5
        self.degCoeffB = 0.5
        self.degCoeffC = 0.5
        self.timeStep = 0.1
        self.iterations = 300
        self.data = {
            'YF1': [self.yf1],
            'PYF1': [self.pyf1],
            'FixJ': [self.fixj],
            'PFixJ': [self.pfixj],
            'CI': [self.ci],
            'TetR': [self.tetr],
            'A': [self.a],
            'B': [self.b],
            'C': [self.c]
        }
        self.timesteps = [0]
        self.visualization = Visualization(self)
        self.visualization.start()

#    def start(self):
#        '''
#        Start the simulation
#        '''
#        pass

    def stop(self):
        '''
        stop the simulation
        '''
        pass

    def cycle(self):
        '''
        Iterates through the simultaion steps
        '''
        '''for i in range(self.MaxTime/self.step + 1):
        '''
        pass

    def getAmount(self, protein):
        '''
        Get the current amount of selected protein
        '''
        return self.data.get(protein)[len(self.data.get(protein)) - 1]

    def derivativeYF1(self, protein):
        return self.promotor1 * self.rbs1 + self.dePhosCoeff1 * self.getAmount('PYF1') - \
                (self.degCoeffYF1 + self.ib) * protein

    def derivativePYF1(self, protein):
        return self.ib * self.getAmount('YF1') - \
                (self.dePhosCoeff1 + self.degCoeffYF1) * protein

    def derivativeFixJ(self, protein):
        return self.promotor1 * self.rbs1 + self.dePhosCoeff2 * self.getAmount('PFixJ') - \
                (self.phosp * self.getAmount('PYF1') + self.degCoeffFixJ) * protein

    def derivativePFixJ(self, protein):
        return self.phosp * self.getAmount('FixJ') * self.getAmount('PYF1') - \
                (self.dePhosCoeff2 + self.degCoeffFixJ) * protein

    def derivativeCI(self, protein):
        return self.promotor2 * self.rbs1 - self.degCoeffCI * protein

    def derivativeTetR(self, protein):
        return (self.promotor3 + self.promotor4) * self.rbs2 - self.degCoeffTetR * protein

    def derivativeA(self, protein):
        return self.promotor3 * self.rbs1 - self.degCoeffA * protein

    def derivativeB(self, protein):
        return self.promotor4 * self.rbs1 - self.degCoeffB * protein

    def derivativeC(self, protein):
        return self.promotor5 * self.rbs1 - self.degCoeffC * protein

    def derivativeSelect(self, name, protein):
        '''
        Select appropriate derivative
        '''
        if name == 'YF1':
            return self.derivativeYF1(protein)
        elif name == 'PYF1':
            return self.derivativePYF1(protein)
        elif name == 'FixJ':
            return self.derivativeFixJ(protein)
        elif name == 'PFixJ':
            return self.derivativePFixJ(protein)
        elif name == 'CI':
            return self.derivativeCI(protein)
        elif name == 'TetR':
            return self.derivativeTetR(protein)
        elif name == 'A':
            return self.derivativeA(protein)
        elif name == 'B':
            return self.derivativeB(protein)
        elif name == 'C':
            return self.derivativeC(protein)

    def promotorUpdate(self):
        self.promotor2 = 5 * self.getAmount('PFixJ')
        self.promotor3 = 1 / (1 + self.getAmount('CI') ** 2)
    #    self.promotor4 =
    #    self.promotor5 =

    def run(self):
        '''
        Runge-Kutta computation for protein concentrations
        '''
        for i in range(self.iterations):
            for key in self.data:
                x = self.getAmount(key)
                coeff1 = self.derivativeSelect(key, x)
                coeff2 = self.derivativeSelect(
                    key, (x + (coeff1) * self.timeStep / 2))
                coeff3 = self.derivativeSelect(
                    key, (x + (coeff2) * self.timeStep / 2))
                coeff4 = self.derivativeSelect(
                    key, (x + (coeff3) * self.timeStep))
                self.data.get(key).append(
                    x + (self.timeStep / 6) * (coeff1 + 2 * coeff2 + 2 * coeff3 + coeff4))
            self.timesteps.append(i + 1)
            self.promotorUpdate()
            self.visualization.update()
            #if i == 50:
            #    self.ib = 0.5
            #    self.promotor2 = 0.5
            #    self.promotor3 = 0
            #    self.promotor4 = 1
            #if i == 100:
            #    self.ib = 1
            #    self.promotor2 = 1
            #    self.promotor4 = 0
            #    self.promotor5 = 1


#    def testY(self):
#        print self.data
#        print self.timesteps

sim = Simulation()

