from UserStuff.User import User
from UserStuff.UserInventory import UserInventory
import datetime

class GameInstance():

	def __init__(self):
		self.sessionTime = 0
		self.sessionStart = None
		self.sessionEnd = None
		self.currentLocation = 'the castle'
		self.startSessionTimer()
		self.myWords = ''

	def startGame(self):
		# define 'me' as the instance of User
		me = User()
		me.inventory = UserInventory()
		me.inventory.populate()
		self.playGame(me)

	def startSessionTimer(self):
		self.sessionStart = datetime.datetime.now()

	def printSessionTime(self):
			self.sessionEnd = datetime.datetime.now()
			print(datetime.timedelta)
			delta = self.sessionEnd-self.sessionStart
			self.sessionTime = delta
			print(self.sessionTime)

	def playGame(self, me):
		print(self.myWords)
		while self.myWords != "quit":
			myWords = self.myWords.lower()
			if(myWords == "show health"):
				me.showHealth()
			elif(myWords == "help"):
				me.showHelpMenu()
			elif(myWords == "heal up"):
				me.healUp(1)
			elif (myWords == "eat a fish"):
				me.eatFish()
			elif(myWords == "take damage"):
				me.takeDamage(4)
				me.showHealth()
			elif(myWords == "session time"):
				self.printSessionTime()
			elif(myWords == "show inventory"):
				me.checkInventory()
			elif(myWords == "go fishing"):
				me.goFishing()
			elif(myWords == "travel away"):
				print("so you don't want to stay at " + self.currentLocation + "...")
				me.listDestinations()
			elif(myWords == "the castle" or myWords == "home"
			or myWords == "the woods" or myWords == "the river"
			or myWords == "the market"):
				self.currentLocation = myWords
				print("you went to " + myWords)
				me.chanceToFindBait()
			elif(myWords == "equipt lure"):
				me.equiptLure()
			elif(myWords != ''):
				print("Sorry, I didn't catch that.")
				print("You can quit by typing quit.")

			self.myWords = input('-->')
