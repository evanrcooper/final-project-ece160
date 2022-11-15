/**
 *
 *	Sample code which provides a proof of concept where 
 *	variables from python are recieved and sent.

░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
 *	
 *	God have mercy
 *
 *	James Ryan, 2022
 */


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>

#include <sys/types.h>
#include <sys/socket.h>

#include <arpa/inet.h>

#include <netinet/in.h>
#include <netinet/ip.h>

//construction of the string.
//made to "emulate" how python's struct functions, so it can be
//unpacked w/ a function call upon arrival.
void cardConstruction(char* toBeSent, int color, int cardNum){
	//format: "<ii"
	//	little endian format, int, int
	//	ex: 2, 2,
	//	out: \x02\x00\x00\x00\x02\x00\x00\x00
	//	sent over network as that, in binary.

	

	return;
}

int main(){
	
	int sock;
	sock = socket(AF_INET, SOCK_STREAM, 0); //localhost, to tcp, 0
	
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(12345); //connects socket to port 5005
	server_address.sin_addr.s_addr = inet_addr("127.0.0.1"); //sets ip to localhost

	int connection = connect(sock, (struct sockaddr *) &server_address, sizeof(server_address));

	if(connection == -1){
		printf("FUCK\n");
		return -127;
	}

	//char conf = 1;
	//send(sock, &conf, sizeof(conf), 0);
	//printf("Sent! Awaiting...\n");

	char server_response[100];
	for(int i = 0; i < 4; i++){
		bzero(server_response, sizeof(server_response));
		read(sock, server_response, sizeof(server_response));
		printf("Server: %X\n", server_response);
		sleep(1);
	}
	close(sock);

	return 0;
}
