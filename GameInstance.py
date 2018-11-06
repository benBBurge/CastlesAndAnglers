from UserStuff.User import User
from UserStuff.UserInventory import UserInventory
import datetime

class GameInstance():

	def __init__(self):
		self.sessionTime = 0
		self.sessionStart = None
		self.sessionEnd = None
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
			myWords = self.myWords
			if(myWords == "show health"):
				me.showHealth()
			elif(myWords == "heal up"):
				me.healUp(1)
			elif(myWords == "take damage"):
				me.takeDamage(1)
			elif(myWords == "session time"):
				self.printSessionTime()
			elif(myWords == "show inventory"):
				me.checkInventory()
			elif(myWords == "go fishing"):
				me.goFishing()
			elif(myWords != ''):
				print("sorry, I didn't catch that")
			
			self.myWords = input('type!')	

	