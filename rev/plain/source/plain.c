#include <stdio.h>
#include <string.h>

int main(int argc, char** argv){
    if (argc < 2){
        puts("Please provide the flag as an arguement ie. \"./plain maple{fake_flag}\"");
        return 0;
    }
    if (strcmp("maple{binaries_are_not_secret}", argv[1]) == 0){
        puts("Correct!");
    } else {
        puts("Try again!");
    }
    return 0;
}