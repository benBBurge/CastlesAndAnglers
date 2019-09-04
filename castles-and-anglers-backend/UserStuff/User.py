from UserStuff.UserInventory import UserInventory
from Activities.Fishing.FishingActivities import FishingActivities
import Activities.Fishing.Fishes #makes the list of fish available
import random

class User():
	def __init__(self):
		self.name = 'New User'
		self.level = 1
		self.maxHealth = 10 * self.level
		self.healthPoints = self.maxHealth - 1
		self.userInventory = UserInventory()
		self.destinationList = ["the river", "home", "the castle", "the market",
		"the woods"]

	def showHealth(self):
		print("Current health: " + str(self.healthPoints) + "hp")

	def healUp(self, amount):
		if (self.healthPoints + amount < self.maxHealth):
			self.healthPoints = self.healthPoints + amount
			print('You healed up to ' + str(self.healthPoints) + ' hp')
		elif (self.healthPoints +amount > self.maxHealth):
			self.healthPoints = self.maxHealth
			print('You have been restored to max health')
		else:
			print('You are at full health already.')

	def takeDamage(self, amount):
		if (self.healthPoints - amount > 0):
			self.healthPoints = self.healthPoints - amount
		elif (self.healthPoints - amount <= 0):
			self.healthPoints = 0
			print('You are already dead and can take no more damage')

	def checkInventory(self):
		print('Inventory contains: ' + str(self.userInventory.listItems()))

	def goFishing(self):
		FishingActivities.goFishing(self)

	def addToInventory(self, item):
		self.userInventory.inventory.append(item)
		print(str(item) + ' added to inventory.')

	def removeFromInventory(self, item):
		self.userInventory.inventory.remove(item)
		print(str(item) + ' removed from inventory.')

# Eat Fish function - asks the user which fish they want to eat.
# If the fish is in their inventory and it is a valid name of
# a fish, the fish will be removed from their inventory and
# HP will increase by 1. - Josh 3/24/19
	def eatFish(self):
		if self.healthPoints == self.maxHealth: 
			print("You can't eat a fish because you're already full!")
		else:
			fish = input("Which fish would you like to eat?")
			fish = fish.title()
			if fish in self.userInventory.inventory:
				if fish in Activities.Fishing.Fishes.Fishes:
					self.healUp(1 + len(fish) % 3)		#variety in HP recovery? 
					self.userInventory.inventory.remove(fish)
				else:
					print("Sorry, that's not a fish!")
			else:
				print("Sorry, you don't have that fish!")

#equipLure() checks to make sure the player has a fishing rod.  If only one type of lure is in the players inventory
#it will be added to the fishing rod without prompt.  If there are multible types, the player will select one.
#might be useful to write another function for checking lure types?  BB 9/4/19

	def equipLure(self):
		if 'fishing rod' not in self.userInventory.inventory:
			print("Fishing rod is already equip with bait")
		else:
			inventoryBait = set(self.userInventory.inventory).intersection(Activities.Fishing.Fishes.Lures)
			if len(inventoryBait) == 1:
				equipment = ''.join(inventoryBait)
				print("Your last piece of bait: " + equipment)
				if equipment == 'bread':
					self.equipBreadRod()
				elif equipment == 'fly':
					self.equipFlyRod()
				elif equipment == 'lure':
					self.equipLuredRod()
				elif equipment == 'worm':
					self.equipWormRod()
			elif len(inventoryBait) > 1:
				strBait = ', '.join(inventoryBait)
				print(strBait)
				equipment = input("equip one of those to fishing rod?\n")
				if equipment == 'bread':
					self.equipBreadRod()
				elif equipment == 'fly':
					self.equipFlyRod()
				elif equipment == 'lure':
					self.equipLuredRod()
				elif equipment == 'worm':
					self.equipWormRod()
			else:
				print("Inventory is devoid of bait.")

	def equipBreadRod(self):
		if 'bread' in self.userInventory.inventory:
			self.removeFromInventory('bread')
			self.removeFromInventory('fishing rod')
			self.addToInventory('bread rod')
		else:
			print("Sorry, you don't have any bread!")

	def equipFlyRod(self):
		if 'fly' in self.userInventory.inventory:
			self.removeFromInventory('fly')
			self.removeFromInventory('fishing rod')
			self.addToInventory('fly rod')
		else:
			print("Sorry, you don't have a lure!")

	def equipLuredRod(self):
		if 'lure' in self.userInventory.inventory:
			self.removeFromInventory('lure')
			self.removeFromInventory('fishing rod')
			self.addToInventory('lured rod')
			#print("Lure added to fishing rod.")
		else:
			print("Sorry, you don't have a lure!")

	def equipWormRod(self):
		if 'worm' in self.userInventory.inventory:
			self.removeFromInventory('worm')
			self.removeFromInventory('fishing rod')
			self.addToInventory('worm rod')
		else:
			print("Sorry, you don't have a worm!")

	def loseLure(self):
		if 'bread rod' in self.userInventory.inventory:
			print("something took the bait")
			self.removeFromInventory('bread rod')
			self.addToInventory('fishing rod')
		elif 'lured rod' in self.userInventory.inventory:
			print("the line snaps and you lose the lure")
			self.removeFromInventory('lured rod')
			self.addToInventory('fishing rod')
		elif 'fly rod' in self.userInventory.inventory:
			print("the bait is lost")
			self.removeFromInventory('fly rod')
			self.addToInventory('fishing rod')
		elif 'worm rod' in self.userInventory.inventory:
			print("something took the bait")
			self.removeFromInventory('worm rod')
			self.addToInventory('fishing rod')		
		else:
			print("You lost a lore you didn't have?  This shouldn't happen.")

	def chanceToFindBait(self):		#had to import .random for this section-- maybe it oculd be moved to fishing activities?
		outcomes = ['worm', 'bread', 'nothing', 'nothing', 'nothing', 'nothing']
		random.shuffle(outcomes)
		currentWormFindingOutcome = outcomes[0]
		if currentWormFindingOutcome != 'nothing':
			print("You find a something on the ground.")
			self.addToInventory(outcomes[0])

	def listDestinations(self):
		print("pick a location to go to:")
		print(self.destinationList)

	def showHelpMenu(self):
		print("Here's what you can do:")
		print("show health")
		print("heal up")
		print("go fishing")
		print("equip lure")
		print("eat a fish")
		print("travel away")
		print("show inventory")
		print("quit")
