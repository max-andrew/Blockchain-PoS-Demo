# proof of stake

import random

# blockchain represented by transaction array "blocks"
# send from, send to, amount
chain = [['sys','max',10], ['sys','andrew',10], ['sys','selma',10], ['andrew','max',6.2], ['max','selma',3.1]]
online = ['selma', 'max','andrew']

# send from, send to, amount
transac_pool = [['max', 'andrew',  .25], ['selma', 'andrew',  .25]]

# read the blockchain and return a list of stakeholders
def findusers():
	users = []
	for i in range(len(chain)):
		if chain[i][1] not in users:
			users.append(chain[i][1])
	return users

# read the blockchain to get the current balance of param stakeholder
def getbalance(stkholder):
	bal = 0
	for i in range(len(chain)):
		if stkholder==chain[i][1]:
			bal += chain[i][2]
		if stkholder==chain[i][0]:
			bal -= chain[i][2]
	return bal

# add transactions from pool to chain if each agent has sufficient funds
def verifyblock():
	selectminer()
	if getbalance(transac_pool[0][0])>=transac_pool[0][2]:
		chain.append(transac_pool[0])
	else:
		print "Error: invalid block, insufficient funds."

# determine which stakeholder will verify the next block
def selectminer():
	# select a weighted random validator (based on stake size)
	stkholds = findusers()
	# outstanding coins
	outst = 30
	# numbered coins of each user
	coins = [10,20,30]

	# determine number of outstanding coins
	for i in range(len(stkholds)):
		outst += getbalance(i)

	# fill coins list
	for i in range(len(stkholds)):
		if i > 0:
			coins.append(getbalance(i)+coins[i-1])
		else:
			coins.append(getbalance(i))

	# get a random number with size equal to coins outstanding
	rand = random.randrange(outst)

	# associate the chosen coin with a user
	for i in range(len(coins)):
		if rand <= coins[i]:
			print(stkholds[i] + " was selected to mine the next block.")
		# if stkholds[i] not in online:
		# 	print("Error: " + stkholds[i] + " is offline and cannot verify transactions.")
		# 	selectminer()

print(chain[len(chain)-1])
verifyblock()
print(chain[len(chain)-1])

# Each block (every 60 seconds), a random Nextcoin is selected to be the next "miner". 
# the odds of a single wallet being selected is the number of coins in that wallet divided by total outstanding coins 
# (Also, it's possible to calculate and agree on who that node is so the transactions need only be sent to that particular wallet.)

# If a node with the selected wallet is running, it will collect the transactions, 
# make a block, and send it to the rest of the network and collect the fees. 
# If the computer is turned off, however, then the entire network will have to 
# select a different nextcoin to make the transaction. 
# This time, the unresponsive wallet will be ignored.