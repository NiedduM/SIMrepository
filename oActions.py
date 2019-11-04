from Tools import *
from Agent import *
from Eagent import *
from Govern import *
from WorldState import *
import pickle as pk

def do1b(address):
    pass


def do2a(address, cycle):
    pass


def do2b(address, cycle):
    pass

def otherSubSteps(subStep, address):
    return False

def showResult(address):

	self = address
	Hg = 0
	T = 0
	C = 0
	for ag in address.modelSwarm.agentList:
		if(type(ag) == Govern):
			G = ag.consumption
			Hg = ag.cash
			T = ag.consumption + Hg
		else:
			C += ag.consumed

	print('Y  ', C + G)
	print('T  ', T)
	print('C  ', C)
	print('H  ', Hg)

	fi = open('SIMmodel/Pickleprove', 'wb')

	db = address.modelSwarm.worldState.db
	pk.dump(db,fi)


