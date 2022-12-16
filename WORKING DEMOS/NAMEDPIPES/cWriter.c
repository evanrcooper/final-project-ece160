#include <stdio.h>

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

//pipe to string
void ptoa(char* buffer, size_t bs, char* p){
	FILE* namedPipe = fopen(p, "r");

	fread(buffer, 
		1, 
		bs, 
		namedPipe
		);
	fclose(namedPipe);
	return;
}

//string to pipe
void atop(char* buffer, size_t bs, char* p){
	FILE* namedPipe = fopen(p ,"w");
	
	fwrite(buffer, 
		1, 
		bs, 
		namedPipe
		);
	fclose(namedPipe);
	return;
}

int main(){
	printf("C: Writing to pipe2...");
	atop("Your Mother\nYour father", 
		sizeof("Your mother\nYour father"),
		"pipe2"
		);	
	printf("done!\n");
	printf("C: waiting for Python on pipe1...");
	char buffer[100];
	ptoa(buffer, 
		sizeof(buffer), 
		"pipe1"
		);
	printf("recv!\n");
	printf("%s",buffer); 

	return 0;
}
