class UserInventory():

	def __init__(self):
			self.inventory = []
			self.startingInventory = ['fishing rod', 'bread', 'bow', 'arrows', 'lure', 'worm']
			self.x = 0
			self.y = 0
			self.populate()

	def listItems(self):
			return self.inventory

	# Not implemented yet: removes an item from the inventory and
	# prints a notification that it's gone. - Josh 3/24/19
	#def removeFromInventory(self, item):
	#	self.userInventory.remove(item)
	#	print(str(item) + ' removed from inventory.')

	def populate(self):
		self.inventory = []
		for item in self.startingInventory:
			self.inventory.append(item)
