import random

# Nextcoin, proof of stake. 

chain = ['gen']
miners = ['max','andrew','selma']
stake = [0.5, 0, 1]
online = [0, 1, 0]

# send from, send to, amount
transactions = {'1': ['max', 'andrew',  .25], '2': ['selma', 'andrew',  .25]}

def selectminer():
	# select a random miner to add
	rand = random.randrange(len(miners))
	print(miners[rand] + " was selected to mine the next block.")
	if online[rand]==0:
		print("Error: " + miners[rand] + " is offline and cannot verify transactions.")
		selectminer()

def verifytransactions():
	# verify? transactions
	print('hello')

selectminer()

# Each block (every 60 seconds), a random Nextcoin is selected to be the next "miner". 
# There are 1 billion coins so the odds of a single wallet being selected is the number of Nxt in that wallet divided by 1 billion. 
# (Also, it's possible to calculate and agree on who that node is so the transactions need only be sent to that particular wallet.)

# If a node with the selected wallet is running, it will collect the transactions, make a block, 
# and send it to the rest of the network and collect the fees. 
# If the computer is turned off, however, then the entire network will have to select a different nextcoin to make the transaction. 
# This time, the unresponsive wallet will be ignored. The network would suffer in that the time to make a block is decreased, 
# but the thought is that people wouldn't leave their computers off if they have a lot of 
# NXT because they're missing out on all the fees that they could have collected.

# If you only have a few NXT, you can leave your computer off: 
# You probably wouldn't have collected much fees anyway. 
# But, your odds of being selected were low so it probably won't decrease transaction times much.