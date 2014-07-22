from math import *


class Simulation(object):
    """docstring for Simulation"""

    def __init__(self):
        '''
        Ask/define the parameters
        '''
        self.arg = 0
        self.yf1 = 0
        self.pyf1 = 0
        self.fixj = 0
        self.pfixj = 0
        self.ci = 0
        self.tetr = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.p1 = 1
        self.p2 = 1
        self.p3 = 1
        self.p4 = 1
        self.p5 = 1
        self.rbs1 = 1
        self.rbs2 = 1
        self.dep1 = 1
        self.dep2 = 1
        self.phosp = 1
        self.ib =  1
        self.hajYF1 = 1
        self.hajFixJ = 1
        self.hajCI = 1
        self.hajTetR = 1
        self.timeStep = 0.2
        self.maxTime =  5
        self.allData = {'YF1':[self.yf1], 'PYF1':[self.pyf1], 'FixJ':[self.fixj], 'PFixJ':[self.pfixj], 'CI':[self.ci], 'TetR':[self.tetr], 'A':[self.a], 'B':[self.b], 'C':[self.c]}

        self.timesteps = 0
        '''self.data = {
            "Dummydata": [1, cos(2), 3, 4, 5, 6, 8, 3, 7, 3, 7, 3],
            "dammydata": [cos(x) for x in self.timesteps]
        }
        pass
        '''
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
        '''for i in range(self.MaxTime/self.step + 1):
        '''
        pass


    def getAmount(self, protein):
        '''
        Get the current amount of selected protein
        '''

        return self.allData.get(protein)[len(self.allData.get(protein))-1]

    def derivativeYF1(self, protein):

        return self.p1*self.rbs1+self.dep1*self.getAmount('PYF1')-(self.hajYF1+self.ib)*protein

    def derivativePYF1(self, protein):

        return self.ib*self.getAmount('YF1')-(self.dep1+self.hajYF1)*protein

    def derivativeFixJ(self, protein):

        return self.p1*self.rbs1+self.dep2*self.getAmount('PFixJ')-(self.phosp*self.getAmount('PYF1')+self.hajFixJ)*protein

    def derivativePFixJ(self, protein):

        return self.phosp*self.getAmount('FixJ')*self.getAmount('PYF1')-(self.dep2+self.hajFixJ)*protein

    def derivativeCI(self, protein):

        return self.p2*self.rbs1-self.hajCI*protein

    def derivativeTetR(self, protein):

        return (self.p3+self.p4)*self.rbs2-self.hajTetR*protein

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

    def rungekutta(self):
        '''
        Runge-Kutta computation for protein concentrations
        '''

        for i in range(int(self.maxTime/self.timeStep) + 1):
            for key in self.allData:
                if key == 'A' or key == 'B' or key == 'C':
                    pass
                else:
                    x = self.getAmount(key)
                    kerroin1 = self.derivativeSelect(key, x)
                    kerroin2 = self.derivativeSelect(key, (x+(kerroin1)*self.timeStep/2))
                    kerroin3 = self.derivativeSelect(key, (x+(kerroin2)*self.timeStep/2))
                    kerroin4 = self.derivativeSelect(key, (x+(kerroin3)*self.timeStep))
                    self.data.get(key).append(x+(self.timeStep/6)*(kerroin1+2*kerroin2+2*kerroin3+kerroin4))


    def testY(self):
        print self.allData

