class Radiateur:
	def __init__(self,etat):
		self.etat = etat
		
	def allumerRadiateur(self):
		self.etat = true
	
	def eteindreRadiateur(self):
		self.etat = false