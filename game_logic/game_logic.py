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
			return None
	# refills deck with cards in the pile (leaves one card as top crad)
	def refillDeck(self):
		temp = self.pile.pop()
		for i in self.pile:
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
	# player to string
	def __str__(self):
		print(self.name, "has", str(len(self.hand)), "cards.")
		print(self.name+"'s hand: ")
		for i in self.hand:
			print(i, end="")
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
game = Game()
game.createGame(int(input("numPlayers: ")))
print(game)
while True:
	break
