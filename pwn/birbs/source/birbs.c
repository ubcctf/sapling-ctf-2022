#include <stdio.h>
#include <stdlib.h>
#include <sys/random.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

char rand_ascii[32];

void cave_exit(){
    system("/bin/sh");
}

int guess_exit(){
    char input [32];    
    long random_num;

    getrandom(&random_num, sizeof(random_num), 0);
    snprintf(rand_ascii, sizeof(rand_ascii), "%ld", random_num);
    puts("Can you guess where the exit is? (A random number from -9223372036854775808 to 9223372036854775807)");
    read(STDIN_FILENO, input, 100);
    if(strncmp(input, rand_ascii, sizeof(rand_ascii)) == 0){
        return 0;
    }
    else {
        return -1;
    }
}

void find_exit(){
    char input[256];
    char option;
    while(1){
        alarm(60);
        puts(
        "Options:\n"
        "1: Try to find the exit.\n"
        "2: Give up."
        );
        fgets(input, sizeof(input), stdin);
        option = input[0];
        if(option == '1'){
            pid_t pid = fork();
            if(pid == 0){
                alarm(60);
                if(guess_exit() == 0){
                    puts("Wow, you found the exit!");
                    cave_exit();
                }
                else{
                    puts("That wasn't the exit. Lets try again.");
                }
                exit(0);
            }
            else if (pid > 0){
                wait(NULL);
            }
        } else if(option == '2') {
            return;
        } else {
            puts("That is not a valid option!");
        }
    }
}

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    find_exit();
    return 0;
}
