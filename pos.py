# proof of stake

# use weighted randomness to select a miner to validate
	# read blockchain to generate a list of users
	# use the balances of each user to determine their likelihood of being selected
# validate a transaction "block" and add to blockchain

# TODO:
# simulate the network using socket programming
	# make validation occur on machine selected
# only allow validation is validator is online
	# ignore unresponsive wallet next round
# automatic validation
	# Each block (every 60 seconds), a random Nextcoin is selected to be the next "miner".
# include transaction fees
# report invalid block added to chain

import random

# blockchain represented by transaction array "blocks"
# send from, send to, amount
chain = [['sys','max',10], ['sys','andrew',10], ['sys','selma',10], ['max','andrew',6], ['max','selma',3]]
online = ['selma', 'max','andrew']

# send from, send to, amount
transac_pool = [['max', 'andrew',  .25], ['max', 'selma',  11], ['selma', 'andrew',  .25]]

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
	# if there are transactions to validate
	if len(transac_pool) > 0:
		selectminer()
		# if user's balance is greater than amount sent
		if getbalance(transac_pool[0][0])>=transac_pool[0][2]:
			# add transaction to chain
			chain.append(transac_pool[0])
			# remove transac from pool
			transac_pool.remove(transac_pool[0])
		else:
			print "Error: invalid block, insufficient funds."
			# remove from pool
			transac_pool.remove(transac_pool[0])
	else:
		print "Error: no transactions to validate."

# determine which stakeholder will verify the next block
def selectminer():
	# select a weighted random validator (based on stake size)
	stkholds = findusers()
	# outstanding coins
	outst = 0
	# numbered coins of each user
	coins = []

	# determine number of outstanding coins
	for i in stkholds:
		outst += getbalance(i)

	# fill coins list
	j = 0
	for i in stkholds:
		# add to last balance if not 0 index
		if j > 0:
			coins.append(getbalance(i)+coins[j-1])
		else:
			coins.append(getbalance(i))
		print(coins)
		j += 1

	# get a random number with size equal to coins outstanding
	rand = random.randrange(outst)

	# throw exception if outstanding coins = 0

	# associate the chosen coin with a user
	j = 0
	for i in coins:
		if rand <= coins[j]:
			print(stkholds[j] + " was selected to mine the next block.")
			# if stkholds[i] not in online:
			# 	print("Error: " + stkholds[i] + " is offline and cannot verify transactions.")
			# 	selectminer()
			break
		j += 1

verifyblock()
print("Most recent block: ") 
print(chain)

verifyblock()
print("Most recent block: ") 
print(chain[len(chain)-1])

verifyblock()
print("Most recent block: ") 
print(chain[len(chain)-1])

verifyblock()
print("Most recent block: ") 
print(chain[len(chain)-1])