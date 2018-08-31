import random

class player:

	def __init__(self, _name, _pNumber):
		self.pname = _name
		self.pNumber = _pNumber
		
	def getMove(param):
		return 1
		
	def getName(self):
		return self.pname
	
	
class randomplayer:

	def __init__(self, _name, _pNumber):
		self.pname = _name
		self.pNumber = _pNumber
	
	def getMove(self, gameState):
		if self.pNumber == 1:
			move = random.randint(0, gameState[0])
		elif self.pNumber == 2:
			move = random.randint(0, gameState[1])
		#print(move)
		return move
		
	def getName(self):
		return self.pname
		
class sequenceplayer:

	def __init__(self, _name, _pNumber):
		self.pname = _name
		self.pNumber = _pNumber
	
	def getMove(self, gameState):
		if gameState[3] > 7: 
			move = 0
		else:
			comp2BidsList = [17, 13, 8, 5, 3, 2, 1, 1]
			move = comp2BidsList[gameState[3]]
		#print(move)
		return move
		
	def getName(self):
		return self.pname
		
class smartplayer:
	def __init__(self, _name, _pNumber):
		self.pname = _name
		self.pNumber = _pNumber
	
	def getMove(self, gameState):
		if self.pNumber == 1:
			mychips = gameState[0]
			oppchips = gameState[1]
			goal = 1
		else:
			mychips = gameState[1]
			oppchips = gameState[0]
			goal = 7
		if oppchips == 0:
			return 1
		if (mychips > (oppchips+1)*abs(goal-gameState[2])):
			#print("round: " + str(gameState[3]) + " and I'm beating " + str(oppchips))
			winningBid = oppchips + 1
			return winningBid
		else:
			if self.pNumber == 1:
				move = random.randint(0, gameState[0])
			elif self.pNumber == 2:
				move = random.randint(0, gameState[1])
			return move		
		
	def getName(self):
		return self.pname
		
		
