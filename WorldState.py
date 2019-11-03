# WorldState.py
from Tools import *
from TFmatrix import *
import pandas as pd

class WorldState(object):
	def __init__(self):

		self.db = pd.DataFrame()

	def collect_data(self):

		self.householdTFM = TFmatrix()
		self.producerTFM = TFmatrix()
		self.governmentTFM = TFmatrix()

		for ag in self.agentList:

			if(ag.agType == 'tastaA'):

				self.householdTFM = self.householdTFM.sumTFM(ag.householdTFM)
				self.producerTFM = self.producerTFM.sumTFM(ag.producerTFM)

			else:

				self.governmentTFM = self.governmentTFM.sumTFM(ag.TFM)
			
