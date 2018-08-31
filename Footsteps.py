import random
from playermodule import player
from playermodule import randomplayer
from playermodule import sequenceplayer
from playermodule import smartplayer

print("Hi! welcome to Quo Vadis\n")
gametype =  0#int(input("What game type? 1=human vs machine, 0=comp vs comp"))
numRounds = 100000
debug=0

if(gametype == 1):
	playing = 1
	while(playing):
		print("You have " + str(playerChips) + " chips and Roboto has " + str(compChips))
		playerBid = int(input("What do you bid?"))
		compBid = random.randint(0, compChips)
		print ("you bid " + str(playerBid) + " and Roboto bid " + str(compBid))
		if(playerBid > compBid): tokenPos-=1
		if(compBid > playerBid): tokenPos+=1
		playerChips -= playerBid
		compChips -= compBid
		
		if tokenPos == 1:
			playing = 0
			print("You Win!!")
		if tokenPos == 7:
			playing = 0
			print("you lose!!")	
	print("Game Over")
	
p1 = randomplayer("Dr Randododo", 1)
p2 = smartplayer("Prof Brainzz", 2)
	 #sequenceplayer("Mr Routin", 2)

results=[0,0,0]
if(gametype == 0):
	for i in range(0, numRounds):		 #number of reps
		gameState = [50, 50, 4, 0]  #This is [player 1s chips, player 2s chips, and the position of the win marker, roundNumber]
		compBidsList = []
		p1List = []
		p2List = []
		playing = 1
		draw = 0
		while(playing):
			p1Bid = p1.getMove(gameState)
			p1List.append(p1Bid)
			p2Bid = p2.getMove(gameState)
			p2List.append(p2Bid)
			if(p2Bid > p1Bid): gameState[2]+=1
			if(p1Bid > p2Bid): gameState[2]-=1
			gameState[1] -= p2Bid
			gameState[0] -= p1Bid
			if gameState[2] == 1:
				playing = 0
				results[0] += 1
				if(debug): print("P1 WINS")
			elif gameState[2] == 7:
				playing = 0
				results[1] += 1
				if(debug): print("P2 WINS")
			elif(gameState[0] == gameState[1] == 0):
				playing = 0
				results[2] += 1
				if(debug): print("DRAW")
			gameState[3] += 1
		if(debug):
			print(p1.getName() + " " + str(p1List))
			print(p2.getName() + " " + str(p2List))
			print("\n")
			
	print(results)


