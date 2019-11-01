from Agent import *
from Govern import *

class Eagent(Agent):

	def __init__(self,number, myWorldState, cash, alpha1, alpha2, workerList, sellerList, agType ,lX=-20, rX=19, bY=-20, tY=19, income = 0, sold=0):

		Agent.__init__(self,number, myWorldState, agType, lX=-20, rX=19, bY=-20, tY=19)

		self.cash = cash
		self.alpha1 = alpha1
		self.alpha2 = alpha2
		self.workersList = workerList
		self.sellerList = sellerList
		self.income = 0
		self.sold = 0
		self.consumed = 0


	def stampa(self):
		print(self.agType)

	def createList_deprecated(self):
		self.sellerList = []
		print('createList method of n.', self.number)
		for ag in self.agentList:
			if(ag.agType == 'tasteA'):
				if(ag.number != self.number):
					self.sellerList.append(ag)
			else:
				self.govern = ag
		i = random.randint(0,len(self.sellerList)-1)
		print(len(self.sellerList))
		ag = self.sellerList[i]
		self.workersList.append(ag)
		print(self.workersList)

	# as household
	def reciveWage(self,wage):

		self.income += wage
		print('n. ', self.number ,'wage received ', self.income)

	def payTaxes(self):
		T = self.govern.taxRate*self.income
		self.govern.receiveTaxes(T)			
		self.income -= T
		

	def consume(self):
		print('n.', self.number, 'I am consuming')
		if(self.income > 0.00001):	#
			c = self.alpha1*self.income
			self.income -= c
			self.consumed += c

			#select a seller
			i = random.randint(0,len(self.sellerList)-1)
			self.sellerList[i].sell(c)
		

	def consumeFromCash(self):
		if(self.cash >0):
			c = self.alpha2*self.cash
			self.cash -= c
			self.consumed += c
			i = random.randint(0,len(self.sellerList)-1)
			self.sellerList[i].sell(c)


	def deposit(self):
		self.cash += self.income
		self.income = 0

	# as producer
	def sell(self, demanded):
		self.sold += demanded
		print('I am reciving ', demanded)

	def payWages(self):
		wage = self.sold/len(self.workersList)
		print(wage)
		for ag in self.workersList:
			ag.reciveWage(wage)
		self.sold = 0
		

