from math import *
from visualize import Visualization
import time
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
        self.promoter1 = 1
        self.promoter2 = 0
        self.promoterA = 1
        self.promoterB = 0
        self.promoterC = 0
        self.rbs1 = 1
        self.rbs2 = 0.75
        self.dePhosCoeff1 = 0.5
        self.dePhosCoeff2 = 0.5
        self.phosp = 1
        self.blue_intensity = 0
        self.red_intensity = 0  # for the intensity switch
        self.degCoeffYF1 = 1
        self.degCoeffFixJ = 1
        self.degCoeffCI = 1
        self.degCoeffTetR = 1
        self.degCoeffA = 0.5
        self.degCoeffB = 0.5
        self.degCoeffC = 0.5
        self.timeStep = 0.1
        self.iterations = 600
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

    def getAmount(self, proteinName):
        '''
        Get the current amount of selected protein
        '''
        return self.data.get(proteinName)[len(self.data.get(proteinName)) - 1]

    def derivativeYF1(self, currentConcentration):
        return self.promoter1 * self.rbs1 + \
            self.dePhosCoeff1 * self.getAmount('PYF1') - \
            (self.degCoeffYF1 + self.blue_intensity) * currentConcentration

    def derivativePYF1(self, currentConcentration):
        return self.blue_intensity * self.getAmount('YF1') - \
            (self.dePhosCoeff1 + self.degCoeffYF1) * currentConcentration

    def derivativeFixJ(self, currentConcentration):
        return self.promoter1 * self.rbs1 + \
            self.dePhosCoeff2 * self.getAmount('PFixJ') - \
            (self.phosp * self.getAmount('PYF1') + self.degCoeffFixJ) * currentConcentration

    def derivativePFixJ(self, currentConcentration):
        return self.phosp * self.getAmount('FixJ') * self.getAmount('PYF1') - \
            (self.dePhosCoeff2 + self.degCoeffFixJ) * currentConcentration

    def derivativeCI(self, currentConcentration):
        return self.promoter2 * self.rbs1 - self.degCoeffCI * currentConcentration

    def derivativeTetR(self, currentConcentration):
        return (self.promoterA + self.promoterB) * self.rbs2 - \
            self.degCoeffTetR * currentConcentration

    def derivativeA(self, currentConcentration):
        return self.promoterA * self.rbs1 - self.degCoeffA * currentConcentration

    def derivativeB(self, currentConcentration):
        return self.promoterB * self.rbs1 - self.degCoeffB * currentConcentration

    def derivativeC(self, currentConcentration):
        return self.promoterC * self.rbs1 - self.degCoeffC * currentConcentration

    def derivativeSelect(self, proteinName, currentConcentration):
        '''
        Select appropriate derivative
        '''
        if proteinName == 'YF1':
            return self.derivativeYF1(currentConcentration)
        elif proteinName == 'PYF1':
            return self.derivativePYF1(currentConcentration)
        elif proteinName == 'FixJ':
            return self.derivativeFixJ(currentConcentration)
        elif proteinName == 'PFixJ':
            return self.derivativePFixJ(currentConcentration)
        elif proteinName == 'CI':
            return self.derivativeCI(currentConcentration)
        elif proteinName == 'TetR':
            return self.derivativeTetR(currentConcentration)
        elif proteinName == 'A':
            return self.derivativeA(currentConcentration)
        elif proteinName == 'B':
            return self.derivativeB(currentConcentration)
        elif proteinName == 'C':
            return self.derivativeC(currentConcentration)

    def promoterUpdate(self):
        self.promoter2 = 7 * self.getAmount('PFixJ')
        self.promoterA = (1 - self.red_intensity) * (1 - self.getAmount('CI'))
        if self.getAmount('CI') < 1:
            self.promoterB = (1 - self.red_intensity) * (self.getAmount('CI'))
        else:
            self.promoterB = (1 - self.red_intensity) * (1 - 2.5 * (self.getAmount('CI') - 1))
        self.promoterC = (1 - self.red_intensity) * (1 - (1.75 / 0.75) * self.getAmount('TetR'))

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
                x = x + (self.timeStep / 6) * (coeff1 + 2 * coeff2 + 2 * coeff3 + coeff4)
                if(x > 0):
                    self.data.get(key).append(x)
                else:
                    self.data.get(key).append(0)
            self.timesteps.append(i + 1)
            self.promoterUpdate()
            self.visualization.update()
        time.sleep(60)

sim = Simulation()
