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


	def createList(self):
		print('createList method of n.', self.number)

		for ag in self.agentList:
			if(ag.agType == 'tasteB'):
				self.govern = ag
				break

		wkProvv = []
		slProvv = []
		for ag in self.agentList:
			if(ag.number in self.workersList):
				wkProvv.append(ag)
			if(ag.number in self.sellerList):
				slProvv.append(ag)

		self.workersList = wkProvv
		self.sellerList = slProvv
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

			#select a seller at random
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
		print('I, n.', self.number, 'am reciving ', demanded)
		#print(self.workerList)

	def payWages(self):
#		if(self.workersList == []):
#			self.workersList.append(self)

		wage = self.sold/len(self.workersList)
		print(wage)
		for ag in self.workersList:
			ag.reciveWage(wage)
		self.sold = 0
		

