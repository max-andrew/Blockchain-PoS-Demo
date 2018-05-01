# Andrew Willis, Max Andrew, Selma Rakovic
# Python 3.7
# Distributed Systems
# 5/1/2018
# Professor Tseng

import random
from time import sleep

# Nextcoin, proof of work. 

# Initial values
chain = ['gen']
miners = ['max','andrew','selma']
wallet = [0.5, 0, 1]
online = [0, 1, 0]
difficulty = 0.5
numTransactions = 2

# send from, send to, amount
# Simulating the blockchain with a dictionary
transactions = {'1': ['max', 'andrew',  .25], '2': ['selma', 'andrew',  .25]}

def mine(id):

	# Computations take time based on difficulty of block mined
	# Simulates this with an increasing sleep over mining attempts
	global difficulty
	sleep(difficulty)

	print(miners[id] + " mined a block for 1 more Nextcoin")
	wallet[id] += 1
	if online[id]==0:
		print("Error: " + miners[id] + " is offline and cannot verify transactions.")
		mine()
	else: difficulty += 1

def make_transaction(fromID,toID,amount):

	# Makes a transaction and adds the transaction to the blockchain
	if(amount > wallet[fromID]):
		print("Don't have enough funds in wallet")
		return False
	wallet[fromID] -= amount
	wallet[toID] += amount
	global numTransactions
	numTransactions += 1
	transactions[str(numTransactions)] = [miners[fromID],miners[toID],amount]
	print("Successful transaction")

def view_transactions():
	for key,value in transactions.items():
		print(key + ": from: " + value[0] + ", to: " + value[1] + ", amount: " + str(value[2]))

# Run User Interface via Powershell or Command Line
id = int(input("Select your id (0,1,2)"))
print("Signed in as: " + miners[id])
print("\nActions you can take:\nmine\nview_wallet\nsign_in\nmake_transaction\nview_transactions\nquit")
while True:
	action = input("\nWhat do you want to do?")
	if(action == "mine"):
		mine(id)
	elif(action == "view_wallet"):
		print("You have " + str(wallet[id]) + " Nextcoin in your wallet")
	elif(action == "sign_in"):
		id = int(input("Select your id (0,1,2)"))
		print("Signed in as: " + miners[id])
	elif(action == "make_transaction"):
		who = int(input("While ID number do you want to make the transaction to?"))
		amount = int(input("How much do you want to give?"))
		make_transaction(id,who,amount)
	elif(action == "view_transactions"):
		view_transactions()
	elif(action == "quit"):
		break

