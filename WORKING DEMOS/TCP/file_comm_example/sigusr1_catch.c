#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void signalHandler(int signum){
	if(signum == SIGUSR1){
		printf("CAUGHT SIGUSR1\n");
	}
	return;
}

//to demo, run "kill -10 <pid>" in another terminal window
int main(int argc, char* argv){
	printf("pid: %d\n",getpid());
	printf("waiting for signal...\n");
	sleep(0.1);

	signal(SIGUSR1, signalHandler);
	pause();
}
