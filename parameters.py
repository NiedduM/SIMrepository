# parameters.py
from Tools import *
import commonVar as common

def loadParameters(self):

    # Projct version
    try:
        projectVersion = str(common.projectVersion)
    except BaseException:
        projectVersion = "Unknown"
    print("\nProject version " + projectVersion)

    #seed of random
    mySeed = eval(input("random number seed (1 to get it from the clock) "))
    if mySeed == 1:
        random.seed()
    else:
        random.seed(mySeed)

    #other instruction necessary to SLAPP
    self.nAgents = 0 
    self.worldXSize = 50
    self.worldYSize = 50


    #simulation data
    common.numberOfPeriods = eval(input('How many reference period?'))
    common.periodLength = eval(input('How many iteration for period?'))
    self.nCycles = common.numberOfPeriods*common.periodLength


    writeSchedule()

    N = common.numberOfAgent
    p = 0.6
    ps = 0.2
    #self.ModelSwarm.workersGraph = nx.erdos_renyi_graph(N, p, directed= True)
    #self.ModelSwarm.sellersGraph = nx.erdos_renyi_graph(N,p,directed = True)







def writeSchedule():


    first = ['all createList','tasteB consume', 'tasteA payWages','tasteA payTaxes', 'tasteA consumeFromCash']
    normal = ['tasteA consume','tasteA deposit','tasteA payWages','tasteA payTaxes']
    end = ['tasteA deposit']
    
    myfile = open('SIMmodel/schedule.txt', 'w')
    
    for period in range(common.numberOfPeriods):

        #initial instructions
        myfile.write('# '+ str(period*common.periodLength+1) + "\n")
        for instruction in first:
            myfile.write(instruction + "\n")
        for instruction in normal:
            myfile.write(instruction + "\n")

        for t in range(1,common.periodLength):
            myfile.write('# '+ str(period*common.periodLength + 1 + t) + "\n")
            for instruction in normal:
                myfile.write(instruction + "\n")

        #end of period instructions
        for instruction in end:
            myfile.write(instruction + "\n") 









