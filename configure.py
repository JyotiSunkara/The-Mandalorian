import os

class Configure:
	'''Details to be printed '''
	def __init__(self):
		self._remainTime = 150
		self._coins = 0 
		self._beamsDestroyed = 0 
		self._lives = 30
		self._enemyLives = 10
		self._shieldOn = 0
		self._start = 0
	
	def setTime(self, value):
		self._remainTime = value

	def setStart(self, value):
		self._start = value

	def getStart(self):
		return self._start

	def changeStart(self, value):
		self._start = self._start + value

	def incrementCoins(self):
		os.system("aplay -q ./music/Coin.wav &")
		self._coins = self._coins + 1

	def getCoins(self):
		return self._coins
	
	def decrementLives(self):
		if self._lives > 0:
			os.system("aplay -q ./music/Death.wav &")
			self._lives = self._lives - 1
		os.system('clear')

	def getLives(self):
		return self._lives
	
	def getTime(self):
		return self._remainTime

	def restart(self):
		os.system('clear')
		self._remainTime = 150
		self._coins = 0 
		self._beamsDestroyed = 0 
		self._enemyLives = 10
		self._remainTime = 150


	def getEnemyLives(self):
		return self._enemyLives

	def enemyLoss(self):
		self._enemyLives = self._enemyLives - 1
		os.system('clear')
