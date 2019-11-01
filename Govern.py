from Agent import*
from Eagent import*

class Govern(Agent):

	def __init__(self,number, myWorldState,cash, consumption, taxRate, agType , lX=-20, rX=19, bY=-20, tY=19, income = 0, sold=0):
	
		Agent.__init__(self,number, myWorldState, agType, lX=-20, rX=19, bY=-20, tY=19)

		self.cash = cash
		self.consumption = consumption
		self.taxRate = taxRate

		#self.balancesheet


	def createList(self):
		self.eagentList = []
		#print('createList method of gov', self.number)
		for ag in self.agentList:
			if(ag.agType == 'tasteA'):
				self.eagentList.append(ag)


	def consume(self):
		demanded = self.consumption/len(self.eagentList)
		#print('gov consumption', demanded)
		for ag in self.eagentList:
			ag.sell(demanded)
		self.cash -= self.consumption

	def receiveTaxes(self, T):
		self.cash += T
