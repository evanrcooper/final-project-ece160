// If it was hard to write, it should be hard to understand.
/*
  ░░      ░░        ░░░░    ▓▓██████████████████████████                              
░░░░██▓▓▓▓              ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                          
░░▓▓░░░░▒▒████▓▓    ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓                      
  ██▓▓░░░░░░░░▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓      ░░████████████
░░▓▓░░▓▓░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░██▓▓░░░░░░░░░░██
░░▓▓░░▓▓░░░░▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░████
░░▓▓░░░░▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░▒▒░░██░░██
░░▓▓░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░▓▓░░░░██
░░▓▓░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░▓▓░░░░██░░░░██
░░▓▓░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░▓▓▒▒██░░░░░░██
  ░░▓▓░░▓▓░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░▒▒▓▓██░░░░██  
  ░░▓▓░░▓▓░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░██░░░░░░██  
    ░░▓▓░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░▓▓░░░░██    
    ░░▓▓░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░▓▓░░░░██    
  ░░░░▓▓░░  ░░░░░░██  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▒▒▓▓██      
    ░░▓▓░░░░░░░░░░██  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▒▒██  ░░    
  ░░▓▓░░░░░░░░░░░░██  ▓▓░░░░  ░░░░  ░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▒▒▓▓  ░░    
  ░░▓▓░░░░░░░░▒▒▓▓    ██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▒▒██        
  ░░▓▓░░░░░░░░▒▒██░░  ██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░▓▓░░░░░░▒▒██        
  ░░▓▓░░░░░░░░▒▒██      ██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░▒▒██        
  ░░▓▓░░░░░░▒▒▒▒░░  ░░  ██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░▒▒██        
  ░░▓▓░░░░░░▒▒▓▓░░      ██░░░░░░░░░░░░░░░░░░▒▒░░██░░░░░░░░░░░░░░▒▒▓▓░░░░░░▒▒██        
  ░░██░░░░░░▒▒▓▓        ░░▓▓░░▒▒░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░▒▒▓▓░░░░░░▒▒██        
  ░░██░░░░░░▒▒▓▓░░        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░░░░▒▒██░░░░░░▒▒██        
  ░░▓▓░░░░▒▒▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓                ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░░░░░▒▒██        
  ░░▓▓▒▒▒▒▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓                      ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓░░▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▓▓▒▒  ▓▓▓▓▓▓▓▓▓▓                      ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓░░▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒░░▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓                      ▓▓▓▓▓▓▓▓▓▓    ▓▓░░▒▒░░░░▒▒██        
  ░░▓▓▒▒▒▒▒▒▓▓    ▓▓░░░░░░▓▓                      ▓▓░░░░░░▓▓    ▓▓▒▒▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▓▓░░░░░░▓▓▓▓▓▓                          ▓▓▓▓▓▓░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒██        
    ▓▓▒▒▒▒▒▒▓▓░░░░░░░░░░░░                          ░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▒▒▒▒  ░░                              ░░      ░░░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓██        
    ▓▓▒▒▒▒▒▒▒▒▓▓                  ▓▓▒▒    ░░              ░░  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓            ▓▓▓▓░░░░▓▓░░                  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓      ▓▓░░░░▓▓  ░░▒▒              ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
  ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
    ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░▓▓    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
    ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░▓▓    ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
    ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░▓▓░░▓▓      ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
    ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▓▓  ▓▓          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██        
    ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░██▓▓░░██      ██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██        
    ░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒██░░░░░░░░░░░░▓▓▓▓      ██  ██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓██        
    ░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒██░░░░░░░░░░░░▓▓▓▓      ████░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██        
      ░░▓▓▒▒██▓▓▒▒▒▒██░░░░░░░░░░▓▓░░░░▓▓░░██░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒██        
        ▓▓▒▒▓▓▓▓▒▒▒▒██░░░░░░░░░░██░░░░▓▓░░██░░░░░░░░██░░██▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▓▓██        
      ░░▓▓▒▒▓▓░░██▒▒▒▒██░░░░░░██░░░░░░░░▓▓░░░░░░░░░░██░░░░██▒▒▒▒▒▒▓▓░░▓▓▒▒▓▓          
      ░░▓▓▒▒▓▓░░▓▓▒▒▒▒▒▒██████░░░░░░░░░░▓▓░░░░░░░░░░██░░░░▓▓▒▒▒▒▒▒▓▓░░██▒▒▒▒          
        ░░▓▓▓▓  ░░██▒▒▒▒▒▒██░░░░░░░░░░░░▓▓░░░░░░░░░░██░░░░██▒▒▒▒▓▓  ░░▓▓▒▒▓▓          
          ░░▓▓    ░░▓▓▒▒▒▒██░░░░░░░░░░░░▓▓░░▓▓░░░░░░░░▓▓░░░░▓▓▓▓░░  ░░▓▓▓▓░░          
            ░░▒▒    ░░▓▓▓▓▓▓░░░░░░░░░░░░▓▓░░░░░░░░░░░░██░░░░▓▓░░    ░░▓▓░░            
            ░░░░▓▓  ░░  ░░██░░░░░░░░░░░░▓▓░░░░░░░░░░░░██░░░░██    ░░▓▓░░              
                        ██░░░░░░░░░░░░▒▒▓▓░░██░░░░░░░░██░░░░░░▓▓░░                    
                        ██░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░██░░░░░░██                      
                        ██░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░██░░░░░░▓▓                    
                        ▓▓░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░██░░░░░░▓▓                    
                        ██░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░▓▓██▓▓██▓▓                    
                        ██████████████▓▓▓▓████████████████      ▓▓                    
                      ▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓██▓▓░░░░                  
                      ▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▓▓▒▒▒▒██░░░░                      
                      ▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒██                          
                      ██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓██▓▓▓▓██                          
                      ░░░░░░▓▓░░░░░░▓▓░░░░░░██░░░░░░▓▓░░░░░░                          
                            ▓▓      ▓▓      ██      ▓▓                                
                            ██▓▓▓▓▓▓▓▓  ░░  ██▓▓▓▓▓▓██                                
                            ▓▓▒▒▒▒▒▒▓▓      ██▒▒▒▒▒▒██                                
                            ██▒▒▒▒▒▒▓▓░░    ██▒▒▒▒▒▒██                                
                            ██▒▒▒▒▒▒▓▓      ██▒▒▒▒▒▒██                                
                            ██▒▒▒▒▒▒▓▓      ██▒▒▒▒▒▒██                                
                            ▓▓▒▒▒▒▒▒▓▓      ██▒▒▒▒▒▒██                                
                            ▓▓▒▒▒▒▒▒▒▒▓▓░░██▒▒▒▒▒▒▒▒██                                
                            ██▒▒▒▒▒▒▒▒▓▓  ▓▓▒▒▒▒▒▒▒▒██                                
                            ░░██▓▓▓▓██▓▓░░▓▓▓▓▓▓▓▓██░░                                
*/

// libraries included
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <ctype.h>

// NUMBER OF PLAYERS DEFINED HERE
#define NUM_PLAYERS 2

// NUMBER OF CARDS DRAWN FOR UNO PUNISHMENT DEFINED HERE
#define UNO_PUNISHMENT 2

// NUMBER OF CARDS DEALT AT THE START OF THE GAME
#define DEAL_AMOUNT 7

// default deck size given standard uno deck
#define DECK_SIZE 108

// array of colors
char colors[5][32] = {"Red", "Blue", "Green", "Yellow", "WILD"};

// card structure
struct card {
	int color;
	char value;
};

// deck structure
struct deck {
	struct card deck[DECK_SIZE]; // cards face-down to draw from (array of cards)
	int deck_size; // size of deck
	struct card pile[DECK_SIZE]; // cards face-up that have been played (array of cards)
	int pile_size; // size of pile
};

// hand structure
struct hand {
	struct card cards[DECK_SIZE]; // cards in hand (array of cards)
	int hand_size; // size of hand
};

// player structure
struct player {
	struct hand hand; // player's hand
	bool uno; // boolean for whether or not the player needed to call uno on their last turn
};

// game structure
struct game {
	struct player players[NUM_PLAYERS]; // array of players in the game
	struct deck main_deck; // main deck to play with
	int current_turn; // current turn (index of player in array of players)
	int order; // turn order (1/-1) clockwise/counterclockwise or forwards/backwards
};

// declaration of all functions
void createDeck(struct deck *deck);
void printDeck(struct deck *deck);
void printPile(struct deck *deck);
void printHand(struct hand *hand);
void printCard(struct card *card);
void printPlayer(struct game *game, int index);
void swapCards(struct deck *deck, int index1, int index2);
void shuffle(struct deck *deck);
struct card draw(struct deck *deck);
void deal(struct game *game);
bool isValidCard(struct deck *deck, struct card *card); 
void computeTurn(struct game *game);
void outputGameState(struct game game);
void takeTurn(struct game *game);
struct card handPull(struct hand *hand, int index);
void handDraw(struct deck *deck, struct hand *hand);
int refillDeck(struct deck *deck);
void cardAction(struct game *game);
int unoInt(char text[], bool *uno);
int inputInt(char text[]);
int inputChar(char text[]);
void inputString(char text[], char *str);
void printColors(void);
int nextPlayer(struct game *game);
void amogus(void);
bool checkWinCondition(struct game *game);

// main function
int main() {
	amogus(); // sus
	srand(time(0)); // starts random number generator with seed of current time

	// creates a game and initializes it
	struct deck deck;
	struct game game;
	game.current_turn = 0;
	game.order = 1;
	game.main_deck = deck;
	createDeck(&(game.main_deck));
	shuffle(&(game.main_deck));
	
	// creates players, initializes them, and deals cards to their hands
	for (int i = 0; i < NUM_PLAYERS; i++) {
		struct player temp_player;
		temp_player.uno = false;
		struct hand temp_hand;
		temp_hand.hand_size = 0;
		temp_player.hand = temp_hand;
		game.players[i] = temp_player;
	}
	deal(&game);

	// prints game state for start of game
	outputGameState(game);	

	// main loop
	while (true) {
		takeTurn(&game); // generic turn function
		computeTurn(&game); // computes next turn index
		outputGameState(game); // prints game state

		// checks win condtition
		if (checkWinCondition(&game)) {
			break;
		}
	}
}

// temp function for int input
int inputInt(char text[]) {
	int temp;
	printf("%s", text);
	if (scanf("%d", &temp) == 1) {;}
	return temp;
}

// temp function for char input
int inputChar(char text[]) {
	char temp;
	printf("%s", text);
	if (scanf("%c", &temp) == 1) {;}
	return temp;
}

// temp function for string intput
void inputString(char text[], char *str) {
	printf("%s", text);
	if (scanf("%s", str) == 1) {;}
}

// initializes deck
void createDeck(struct deck *deck) {
	deck->pile_size = 0;
	int index = 0; // stores current index of deck to append cards
	struct card temp_card;

	// loops through each color
	for (int i = 0; i < 4; i++) {
		temp_card.color = i;
		for (int j = 0; j < 10; j++) { // 0-9
			temp_card.value = j+'0';
			deck->deck[index++] = temp_card;
		}
		for (int j = 1; j < 10; j++) { // 1-9
			temp_card.value = j+'0';
			deck->deck[index++] = temp_card;
		}
		temp_card.value = 'S'; // skip
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
		temp_card.value = 'R'; // revese
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
		temp_card.value = '+'; // draw 2
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
	}
	temp_card.color = 4; // wild card
	temp_card.value = 'P'; // draw 4
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 4; j++) {
			deck->deck[index++] = temp_card;
		}
		temp_card.value = 'C'; // color change
	}
	deck->deck_size = index;
}

// prints deck from struct deck
void printDeck(struct deck *deck) {
	for (int i = 0; i < deck->deck_size; i++) {
		printf("#%d, Color = %s, Value = %c\n", i, colors[deck->deck[i].color], deck->deck[i].value);
	}
}

// prints pile from struct pile
void printPile(struct deck *deck) {
	for (int i = 0; i < deck->pile_size; i++) {
		printf("#%d, Color = %s, Value = %c\n", i, colors[deck->pile[i].color], deck->pile[i].value);
	}
}

// prints struct hand
void printHand(struct hand *hand) {
	for (int i = 0; i < hand->hand_size; i++) {
		printf("#%d, Color = %s, Value = %c\n", i, colors[hand->cards[i].color], hand->cards[i].value);
	}
}

// prints struct card
void printCard(struct card *card) {
	if (card->value == 'P') {
		char print_value[] = "";
	} else if (card->value == 'C') {
		char print_value[] = "Change Color";
	} else if (card->value == 'P') {
		char print_value[] = "Draw 4";
	} else if (card->value == 'S') {
		char print_value[] = "Skip";
	} else if (card->value == 'R') {
		char print_value[] = "Reverse";
	} else if (card->value == '+') {
		char print_value[] = "+2";
	} else {
		char print_value[] = card->value;
	}
	printf("Color = %s, Value = %s\n", colors[card->color], print_value);
}

// prints struct player
void printPlayer(struct game *game, int index) {
	if (index >= NUM_PLAYERS || index < 0) {
		printf("Error: Index Out Of Bounds\n");
		return;
	}
	printf("Player %d's Hand:\n", index);
	printHand(&(game->players[index].hand));
}

// swaps two cards in the deck
void swapCards(struct deck *deck, int index1, int index2) {
	struct card temp_card = deck->deck[index1];
	deck->deck[index1] = deck->deck[index2];
	deck->deck[index2] = temp_card;
}

// shuffles the deck
void shuffle(struct deck *deck) {
	// loops through the deck and switches it with another random card in the deck
	for (int i = 0; i < deck->deck_size; i++) {	
		swapCards(deck, i, rand()%deck->deck_size);
	}
}

// pops and returns the top card of the deck
struct card draw(struct deck *deck) {
	deck->deck_size -= 1;
	return deck->deck[deck->deck_size];
}

// deals cards to each player
void deal(struct game *game) {
	for (int i = 0; i < NUM_PLAYERS; i++) {
		for (int j = 0; j < DEAL_AMOUNT; j++) {
			game->players[i].hand.cards[game->players[i].hand.hand_size++] = draw(&(game->main_deck));
		}
	}
	game->main_deck.pile[game->main_deck.pile_size++] = draw(&(game->main_deck));
}

// compares a card with the top card of the deck to see if it is playable
bool isValidCard(struct deck *deck, struct card *card) {
	if (deck->pile[deck->pile_size-1].color == card->color) { // matching color
		return true;
	} else if (deck->pile[deck->pile_size-1].value == card->value) { // matching value
		return true;
	} else if (card->color == 4 || deck->pile[deck->pile_size-1].color == 4) { // wild card
		return true;
	}
	return false;
}

// computes next turn
void computeTurn(struct game *game) {
	game->current_turn += game->order;
	if (game->current_turn < 0) {
		game->current_turn = NUM_PLAYERS-1;
	} else if (game->current_turn >= NUM_PLAYERS) {
		game->current_turn = 0;
	}
}

// prints the current game state
void outputGameState(struct game game) {
	// prints every players hands
	for (int i = 0; i < NUM_PLAYERS; i++) {
		printf("Player #%d's Hand:\n", i);
		for (int j = 0; j < game.players[i].hand.hand_size; j++) {
			printf("Card #%d: %s %c\n", j, colors[game.players[i].hand.cards[j].color], game.players[i].hand.cards[j].value);
		}
		printf("\n");
	}

	// prints current turn and order
	printf("Player %d's turn.\n", game.current_turn);
	if (game.order == 1) {
		printf("The turn order is forwards.\n");
	} else if (game.order == -1) {
		printf("The turn order is backwards.\n");
	}

	// prints size of deck and pile
	printf("There are/is currently %d card(s) left in the deck.\n", game.main_deck.deck_size);
	printf("There are/is currently %d card(s) in the pile.\n", game.main_deck.pile_size);
	printf("\n");
	
	// prints top card in the pile
	printf("Top card in the pile: %s %c\n", colors[game.main_deck.pile[game.main_deck.pile_size-1].color], game.main_deck.pile[game.main_deck.pile_size-1].value);
	printf("\n");
}

// turn function for every player
void takeTurn(struct game *game) {
	// resets uno value (if player went full round without getting caught they do not need to call uno again)
	game->players[game->current_turn].uno = false;
	
	// initializes variables
	bool UNO; // stores whether the player called uno or not
	bool playedCard = false; // stores whether the player played a card or not this turn
	int index; // stores index of the card from the players hand that their playing
	bool draw = false; // stores whether the player needs to draw from the deck
	bool hasValidCard = false; // stores whether the player has a valid card in their hand to play
	
	// gets initial input for index of card to play (including if they call uno)
	do {
		index = unoInt("Card Index: ", &UNO);
		if (index < 0 && !draw) { // if player chooses to draw (and doesn't have a valid card)
			for (int i = 0; i < game->players[game->current_turn].hand.hand_size; i++) {
				if (isValidCard(&(game->main_deck), &(game->players[game->current_turn].hand.cards[i]))) {
					hasValidCard = true;
				}
			}
			if (!hasValidCard) { // if player doesn't have a valid card they can draw
				draw = true;
			}
		} else if (index < game->players[game->current_turn].hand.hand_size) { // if player has a valid card get the card index
			if (isValidCard(&(game->main_deck), &(game->players[game->current_turn].hand.cards[index]))) {
				game->main_deck.pile[game->main_deck.pile_size++] = handPull(&(game->players[game->current_turn].hand), index);
				playedCard = true;
				break;
			}
		}
	} while (!draw);

	// draws cards if player needs to draw
	while (draw) {
		if (game->main_deck.deck_size == 0) {
			if (refillDeck(&(game->main_deck)) != 0) {
				handDraw(&(game->main_deck), &(game->players[game->current_turn].hand));
				printCard(&(game->players[game->current_turn].hand.cards[game->players[game->current_turn].hand.hand_size-1]));
			} else {
				break;
			}
		} else {
			handDraw(&(game->main_deck), &(game->players[game->current_turn].hand));
			printCard(&(game->players[game->current_turn].hand.cards[game->players[game->current_turn].hand.hand_size-1]));
		}
		// draws until the player draws a valid card or the deck runs out of cards
		if (isValidCard(&(game->main_deck), &(game->players[game->current_turn].hand.cards[game->players[game->current_turn].hand.hand_size-1]))) {
			if (inputInt("Play Drawn Card (1/0 = Y/N): ") == 1) { // asks the player if they want to play their drawn card
				game->main_deck.pile[game->main_deck.pile_size++] = handPull(&(game->players[game->current_turn].hand), game->players[game->current_turn].hand.hand_size-1);
				playedCard = true;
			}
			draw = false;
		}
	}

	// checks if player needed to call uno and didn't
	if (game->players[game->current_turn].hand.hand_size == 1 && !UNO) {
		game->players[game->current_turn].uno = true;
	}

	// if player calls uno checks each previous player to see if any need to draw the uno punishment
	if (UNO) {
		for (int i = 0; i < NUM_PLAYERS; i++) {
			if (game->players[i].uno == true && i != game->current_turn) {
				for (int j = 0; j < UNO_PUNISHMENT; j++) {
					if (game->main_deck.deck_size == 0) {
						if (refillDeck(&(game->main_deck)) != 0) {
							handDraw(&(game->main_deck), &(game->players[i].hand));
						} else {
							break;
						}
					} else {
						handDraw(&(game->main_deck), &(game->players[i].hand));
					}
				}
			}	
		}
	}

	// if player played a card executes the card action (ex: reverses order if reverse card is played)
	if (playedCard) {
		cardAction(game);
	}
}

// pulls and returns a card from hand
struct card handPull(struct hand *hand, int index) {
	struct card pulled_card = hand->cards[index];
	hand->hand_size--;
	for (int i = 0; i < hand->hand_size-index; i++) {
		hand->cards[i+index] = hand->cards[i+index+1];
	}
	return pulled_card;
}

// appends card to hand 
void handDraw(struct deck *deck, struct hand *hand) {
	hand->cards[hand->hand_size++] = draw(deck);
}

// refills the deck with all the cards in the pile except the top card
int refillDeck(struct deck *deck) {
	int i = 0;
	for ( ; i < deck->pile_size-1; i++) {
		if (deck->pile[i].value == 'C' || deck->pile[i].value == 'P') {
			deck->pile[i].color = 4;
		}
		deck->deck[deck->deck_size++] = deck->pile[i];
	}
	deck->pile[0] = deck->pile[deck->pile_size-1];
	deck->pile_size = 1;
	shuffle(deck);
	return i; // returns number of cards added to the deck
}

// executes action needed for special cards
void cardAction(struct game *game) {
	int temp_color, draw = 0;

	// if wild card get new color
	if (game->main_deck.pile[game->main_deck.pile_size-1].value == 'C' || game->main_deck.pile[game->main_deck.pile_size-1].value == 'P') {
		printColors();
		do {
			temp_color = inputInt("New Color: ");
		} while (temp_color < 0 || temp_color > 3);
		game->main_deck.pile[game->main_deck.pile_size-1].color = temp_color;
	}
	
	// if reverse and there are more than 2 players then reverse the turn order and if there are 2 players then skip turn
	if (game->main_deck.pile[game->main_deck.pile_size-1].value == 'R') {
		if (NUM_PLAYERS > 2) {
			game->order *= -1;
		} else {
			computeTurn(game);
		}

	// if skip then skip next turn
	} else if (game->main_deck.pile[game->main_deck.pile_size-1].value == 'S') {
		computeTurn(game);
	
	// if draw 2 or draw 4 then draw those cards to next players hand and skips turn
	} else if (game->main_deck.pile[game->main_deck.pile_size-1].value == '+' || game->main_deck.pile[game->main_deck.pile_size-1].value == 'P') {
		draw = game->main_deck.pile[game->main_deck.pile_size-1].value == 'P' ? 4 : 2;
	}
	for (int i = 0; i < draw; i++) {
		if (game->main_deck.deck_size == 0) {
			if (refillDeck(&(game->main_deck)) != 0) {
				handDraw(&(game->main_deck), &(game->players[nextPlayer(game)].hand));
			} else {
				break;
			}
		} else {
			handDraw(&(game->main_deck), &(game->players[nextPlayer(game)].hand));
		}
	}
	if (draw > 0) {
		computeTurn(game);
	}
}

// given input extracts whether uno was called with an int
int unoInt(char text[], bool *uno) {
	int val, count, i;
	val = count = i = 0;
	char phrase_upper[] = "UNO";
	char phrase_lower[] = "uno";
	printf("%s", text);
	char c = getchar();
	char last = '\0';
	while (!isdigit(c)) {
		if (i <= 2) {
			if (c == phrase_lower[i] || c == phrase_upper[i]) {
				count += 1;
			}
		}
		last = c;
		c = getchar();
		i++;
	}
	while (isdigit(c)) {
		val *= 10;
		val += c-'0';
		c = getchar();
	}
	if (last == '-') {
		val *= -1;
	}
	*uno = count >= 3;
	return val;
}

// prints all available colors
void printColors(void) {
	for (int i = 0; i < 4; i++) {
		printf("%d = %s, ", i, colors[i]);
	}
	printf("\n");
}

// gets index of next player without updating current turn
int nextPlayer(struct game *game) {
	if (game->current_turn+game->order < 0) {
		return NUM_PLAYERS-1;
	} else if (game->current_turn+game->order >= NUM_PLAYERS) {
		return 0;
	} else {
		return game->current_turn+game->order;
	}
}

// sus
void amogus(void) {
	/*
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
 ⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	*/
}

// checks if any players have no cards left in their hand and prints winner if any
bool checkWinCondition(struct game *game) {
	for (int i = 0; i < NUM_PLAYERS; i++) {
		if (game->players[i].hand.hand_size == 0) {
			printf("\nPlayer #%d Wins!\n", i);
			return true;
		}
	}
	return false;
}
