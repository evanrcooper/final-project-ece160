# random library for shuffling deck
import random

# colors for printing (list)
colors = ["Red", "Green", "Blue", "Yellow", "Wild"]

# values for printing (dict)
values = {
	"0": "0",
	"1": "1",
	"2": "2",
	"3": "3",
	"4": "4",
	"5": "5",
	"6": "6",
	"7": "7",
	"8": "8",
	"9": "9",
	"S": "Skip",
	"R": "Reverse",
	"+": "+2",
	"C": "Change Color",
	"P": "+4"
}

# card class
class Card:
	# init with value and color
	def __init__(self, value, color):
		self.value = value
		self.color = color
	# checks if card is wild card
	def isWild(self):
		if self.color == 4:
			return True
		return False
	# checks if card is a number card
	def isNum(self):
		if self.value in "0123456789":
			return True
		return False
	# card to string for printing
	def __str__(self):
		print(colors[self.color], values[self.value])
		return ""
	def hasAttribute(self):
		if self.isNum():
			return False
		else:
			return True
# main deck class
class MainDeck:
	#init with empty pile (face up) to play to and deck (face down) to darw from
	def __init__(self):
		self.deck = []
		self.pile = []
	# main deck to string for printing
	def __str__(self):
		print("Number of cards in the deck: ", str(len(self.deck)))
		print("Cards in the deck:\n")
		for i in self.deck:
			print(i, end="")
		print("\nNumber of cards in the pile: ", str(len(self.pile)))
		print("Cards in the pile:")
		for i in self.pile:
			print(i)
		print()
		return ""
	# draw function pops card from top of deck
	def draw(self):
		if len(self.deck) > 0:
			return self.deck.pop()
		else:
			self.refillDeck()
			if len(self.deck) > 0:
				return self.deck.pop()
			else:
				return None
	# refills deck with cards in the pile (leaves one card as top card)
	def refillDeck(self):
		temp = self.pile.pop()
		for i in self.pile:
			if i.value in "PC":
				new_wild = i
				new_wild.color == 4
				self.deck.append(new_wild)
			else:
				self.deck.append(i)
		self.pile = [temp]
	# checks if input card is valid to play on top of top() card
	def isValidCard(self, card):
		if card.isWild():
			return True
		elif self.top().color == card.color:
			return True
		elif self.top().value == card.value:
			return True
		else:
			return False
	# returns card at the top of the pile
	def top(self):
		return self.pile[len(self.pile)-1]

# player class
class Player:
	# init with name and empty hand
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.needs_uno = False
	# player to string
	def __str__(self):
		print(self.name, "has", str(len(self.hand)), "cards.")
		print(self.name+"'s hand: ")
		for i, ele in enumerate(self.hand):
			print(str(i+1), ". ", ele, sep="", end="")
		print()
		return ""
# game class
class Game:
	#init with list of players, main deck, current turn (0 - playerCount-1), and turn order (-1, 1)
	def __init__(self):
		self.players = []
		self.main_deck = MainDeck()
		self.current_turn = 0
		self.order = 1
	# game to string
	def __str__(self):
		print("Players:")
		for i in self.players:
			print(i)
		print("\nMain Deck:", self.main_deck, sep="\n")
		print("Current Turn:", self.players[self.current_turn].name)
		if self.order == 1:
			print("\nTurn order is forwards.")
		else:
			print("\nTrun order is backwards.")
		return ""
	# add player to list of players
	def addPlayer(self, player):
		self.players.append(player)
	# shuffles deck
	def shuffleDeck(self):
		random.shuffle(self.main_deck.deck)
	# creates new deck for start of game (adds/creates all cards needed)
	def createDeck(self):
		for i in range(4):
			self.main_deck.deck.append(Card("0", i))
			for x in range(2):
				self.main_deck.deck.append(Card("S", i))
				self.main_deck.deck.append(Card("R", i))
				self.main_deck.deck.append(Card("+", i))
			for y in range(9):
				self.main_deck.deck.append(Card(str(y+1), i))
		for j in range(2):
			self.main_deck.deck.append(Card(str("C"), 4))
			self.main_deck.deck.append(Card(str("P"), 4))
		random.shuffle(self.main_deck.deck)
	# creates the game (gets player data, creates deck, and deals cards)
	def createGame(self, numPlayers):
		for i in range(numPlayers):
			self.players.append(Player(input("Player #"+str(i+1)+"\'s name: ")))
		self.createDeck()
		index = 0
		self.deal()
		for i in self.main_deck.deck:
			if not i.isNum():
				index += 1
			else:
				self.main_deck.pile.append(i)
				self.main_deck.deck.pop(index)
				break
		self.shuffleDeck()
	# deals 7 cards to all players
	def deal(self):
		for i in self.players:
			for j in range(7):
				i.hand.append(self.main_deck.draw())
	# updates turn based on turn order
	def updateTurn(self):
		self.current_turn += self.order
		if self.current_turn >= len(self.players):
			self.current_turn = 0
		elif self.current_turn < 0:
			self.current_turn = len(self.players)-1
	# prints the info needed for each turn
	def printTurn(self):
		print("Top Card In Pile: ")
		print(self.main_deck.top())
		print()
		print(self.players[self.current_turn].name, "\'s turn: ", sep="")
		print(self.players[self.current_turn])
	# compares all cards of player whose turn it is to top of pile to see if they have a valid card
	def hasValidCard(self):
		for i in self.players[self.current_turn].hand:
			if self.main_deck.isValidCard(i):
				return True
		return False
	# returns index of player whose turn it is next
	def nextTurn(self):
		self.updateTurn()
		nt = self.current_turn
		self.order *= -1
		self.updateTurn()
		self.order *= -1
		return nt
	# changes color of card thats down
	def changeColor(self):
		new_color = int(input("New Color: "))
		while not new_color in range(4):
			new_color = int(input("New Color: "))
		self.main_deck.pile[len(self.main_deck.pile)-1].color = new_color
	# if card isnt a number card does the action required for that card
	def doAttribute(self):
		top = self.main_deck.top()
		nt = self.nextTurn()
		if top.value == "+":
			for i in range(2):
				self.players[nt].hand.append(self.main_deck.draw())
		elif top.value == "P":
			for i in range(4):
				self.players[nt].hand.append(self.main_deck.draw())
				self.changeColor()
		elif top.value == "S":
			self.updateTurn()
		elif top.value == "R":
			if len(self.players) == 2:
				self.updateTurn()
			else:
				self.order *= -1
		elif top.value == "C":
			self.changeColor()
			
# creates game with inputted number of players
game = Game()
game.createGame(int(input("Number of Players: ")))

# main loop
while True:
	# temporary variables
	card_played = False # stores whether the player played a card or not
	uno = False # stores whether the player called uno or not
	# prints info for current players turn
	game.printTurn()
	# gets index of current player
	ct = game.current_turn
	# gets card to be played
	card_index = int(input("Card To Play (0 To Draw): "))-1
	# checks if player has a valid card
	if game.hasValidCard():
		# makes sure the card theyre playing is valid and doesnt let them draw
		while True:
			# plays the card they chose
			if game.main_deck.isValidCard(game.players[ct].hand[card_index]):
				game.main_deck.pile.append(game.players[ct].hand.pop(card_index))
				card_played = True
				# does the card's action/attribute
				if game.main_deck.top().hasAttribute():
					game.doAttribute()
				break
			else:
				card_index = int(input("Card To Play (0 To Draw): "))-1
	# if player has no valid cards they must draw
	else:
		while card_index != -1:
			card_index = int(input("Card To Play (0 To Draw): "))-1
	# draw until they get a valid card or run out of cards
	if card_index == -1:
		while True:
			drawn = game.main_deck.draw()
			# makes sure deck isnt empty
			if drawn is not None:
				game.players[ct].hand.append(drawn)
				if game.main_deck.isvalidCard(drawn):
					# checks if they want to play the drawn cards
					to_play = int(input("Play Drawn Card? (1=Yes, 0=No): "))
					if to_play == 1:
						game.main_deck.pile.append(game.players[ct].hand.pop(len(game.players[ct].hand)-1))
						card_played = True
						if game.main_deck.top().hasAttribute():
							game.doAttribute()
						break
					else:
						break
			else:
				break
	# asks if they want to call uno
	if int(input("Call UNO? (1=Yes, 0=No): ")) == 1:
		uno = True
	# checks if they needed to call uno 
	if card_played:
		# checks if player won
		if len(game.players[ct].hand) == 0:
			break
		elif len(game.players[ct].hand) == 1:
			if not uno:
				gane.players[ct].needs_uno = True
	# if uno was called distributes uno penalty to other players who didn't call it
	if uno:
		for i in game.players:
			if i.needs_uno:
				i.needs_uno = False
				for j in range(2):
					card_drawn = game.main_deck.draw()
					if card_drawn is None:
						break
					else:
						i.hand.append(card_drawn)
	# updates current turn to next player
	game.updateTurn()
for i in game.players:
	if len(i.hand) == 0
	print(i.name, "Wins!")
	break
