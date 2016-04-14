class Capteur:
	def __init__ (self,valeur):
		self.valeur = valeur
		
	def getEtat(self):
		return self.valeur
		
	def setEtat(self,valeur):
		self.valeur=valeur
