#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DECK_SIZE 108
#define NUM_PLAYERS 4

struct card {
	int color;
	char value;
};

struct deck {
	struct card deck[DECK_SIZE];
	int deck_size;
	struct card pile[DECK_SIZE];
	int pile_size;
};

struct hand {
	struct card cards[DECK_SIZE];
	int hand_size;
};

struct player {
	struct hand hand;
};

struct game {
	struct player players[NUM_PLAYERS];
	struct deck main_deck;
	int current_turn;
};

void createDeck(struct deck *deck);
void printDeck(struct deck *deck);
void printPile(struct deck *deck);
void printHand(struct hand *hand);
void printCard(struct card *card);
void swapCards(struct deck *deck, int index1, int index2);
void shuffle(struct deck *deck);
struct card draw(struct deck *deck);
void deal(struct game *game);


int main() {
	srand(time(0));
	struct deck deck;
	struct game game;
	game.main_deck = deck;
	createDeck(&(game.main_deck));
	shuffle(&(game.main_deck));
	for (int i = 0; i < NUM_PLAYERS; i++) {
		struct player temp_player;
		struct hand temp_hand;
		temp_hand.hand_size = 0;
		temp_player.hand = temp_hand;
		game.players[i] = temp_player;
	}
	deal(&game);
}

void createDeck(struct deck *deck) {
	deck->pile_size = 0;
	int index = 0;
	struct card temp_card;
	for (int i = 0; i < 4; i++) { //4 Colors
		temp_card.color = i;
		for (int j = 0; j < 10; j++) { //0-9
			temp_card.value = j+'0';
			deck->deck[index++] = temp_card;
		}
		for (int j = 1; j < 10; j++) { //1-9
			temp_card.value = j+'0';
			deck->deck[index++] = temp_card;
		}
		temp_card.value = 'S'; //Skip
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
		temp_card.value = 'R'; //Revese
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
		temp_card.value = 'D'; //Draw 2
		deck->deck[index++] = temp_card;
		deck->deck[index++] = temp_card;
	}
	temp_card.color = 5; //Wild Card
	temp_card.value = '+'; //Draw 4
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	temp_card.value = 'C'; //Color Change
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	deck->deck[index++] = temp_card;
	deck->deck_size = index;
}

void printDeck(struct deck *deck) { //Debug print deck
	for (int i = 0; i < deck->deck_size; i++) {
		printf("#%d, Color = %d, Value = %c\n", i, deck->deck[i].color, deck->deck[i].value);
	}
}

void printPile(struct deck *deck) { //Debug print pile
	for (int i = 0; i < deck->pile_size; i++) {
		printf("#%d, Color = %d, Value = %c\n", i, deck->pile[i].color, deck->pile[i].value);
	}
}

void printHand(struct hand *hand) { //Debug print hand
	for (int i = 0; i < hand->hand_size; i++) {
		printf("#%d, Color = %d, Value = %c\n", i, hand->cards[i].color, hand->cards[i].value);
	}
}

void printCard(struct card *card) {
	printf("Color = %d, Value = %c\n", card->color, card->value);
}

void swapCards(struct deck *deck, int index1, int index2) {
	struct card temp_card = deck->deck[index1];
	deck->deck[index1] = deck->deck[index2];
	deck->deck[index2] = temp_card;
}

void shuffle(struct deck *deck) {
	for (int i = 0; i < deck->deck_size; i++) {	
		swapCards(deck, i, rand()%deck->deck_size);
	}
}

struct card draw(struct deck *deck) {
	deck->deck_size--;
	return deck->deck[deck->deck_size];
}

void deal(struct game *game) {
	for (int i = 0; i < NUM_PLAYERS; i++) {
		for (int j = 0; j < 7; j++) {
			game->players[i].hand.cards[game->players[i].hand.hand_size++] = draw(&(game->main_deck));
		}
	}
}
