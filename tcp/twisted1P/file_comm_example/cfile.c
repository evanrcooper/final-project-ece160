
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <ctype.h>
#include <unistd.h>

#define DECK_SIZE 108
#define NUM_PLAYERS 2
#define TURNS 15
#define UNO_PUNISHMENT 2

//we want to WRITE to py_readin
//we want to READ from c_readin
//capiche?
#define C_READIN "./c_readin"
#define PY_READIN "./py_readin"
//we are wasteful in this household. ALL THE MEMORY!!!!!
#define READINBUFFER 10000
	
char py_readin[READINBUFFER];
unsigned int py_readinSIZE = 0;
char c_readin[READINBUFFER];
unsigned int c_readinSIZE = 0;

unsigned int c_readinChecksum = 0;
unsigned int py_readinChecksum = 0;

void writeToPyReadin(char text[]);
void readFromCReadin(void);
void clearBuffer(char buf[], unsigned int* length);

//Waits for an update
void waitForResponse(void);
//checksums a file and sees if it changes
unsigned char changeIn(FILE* file);

void writeToPyReadin(char* text){
	FILE* py_in; //Note the distinction: PY_READIN is a path! py_readin points to the file 
	char c;

	py_in = fopen(PY_READIN, "w");

	if(py_in == NULL){
		printf("writeToPyReadin: py_readin cannot be opened/created.\n");
		return;
	}
	
	int i = 0;
	do{
		c = text[i];
		fputc(c, py_in);
		printf("%c", c);
		i++;
	} while(i != strlen(text));

	fclose(py_in);
	return;
}

void readFromCReadin(){
	FILE* c_in;
	char c;

	c_in = fopen(C_READIN, "r");

	if(c_in == NULL){
		printf("readFromCReadin: c_readin cannot be opened. My bowels will now evacuate onto the kitchen floor.\nIn the current directory, please run the provided init.sh script.\n");
		return;
	}

	//Buffer management; clean up what once was	
	clearBuffer(c_readin, &c_readinSIZE);

	unsigned int i = 0;
	do{
		c = fgetc(c_in);
		c_readin[i] = c; //refers to global buffer list
		i++;
	} while(c != EOF);
	
	c_readinSIZE = i;
	fclose(c_in);
	
	return; 
}

//https://stackoverflow.com/a/3464166
//REMEMBER TO CLOSE THE FILE!!!!!
unsigned char checksumOfString(char *text){
	unsigned char cs = 0;

	int i = 0;
	while (text[i] != '\0') {
		cs ^= text[i];
		i++;
	}
	//printf("%d", cs);
	return cs;
}

//Stick in one of the global buffers and its respective length
//It will become empty
void clearBuffer(char buf[], unsigned int* length){
	while(*length>0){
		buf[*length-1] = '0';
		*length--;
	}

	return;
}

void initCPythComms(void){
	printf("---START C-PYTH SETUP---\n");
	printf("Writing to Python, letting know I'm ready...\n");
	writeToPyReadin("1");
	
	printf("Waiting for a response from python...");


	return;
}

int changeInCReadin(){
	readFromCReadin();
	long unsigned int cs = checksumOfString(c_readin);
	if(cs != c_readinChecksum){
		sleep(2);	

		return 0;
	}
	return 1;
}

int main() {
	printf("start shit");
	initCPythComms();

	//Example: 
	//C writes to py readin, while python waits
	//Python realizes, python writes to c readin
	//C realizes, writes to py readin
	char arrOf[3][10] = {"garbage", "c is cool", "6^7*{{}"};
	int i = 0;
	while(1){
		//We'll have C start
		//Python can wait
		writeToPyReadin(arrOf[i]);
		printf("Waiting for changes...");
		while(!changeInCReadin());
		i++;
		if(i == 2) break;
	}
	return 0;
}

