const char key[] = "\x4a\x83\x04\xd5";
const char enc_flag[] = "\x27\xe2\x74\xb9\x2f\xf8\x70\xbd\x79\xdc\x4f\x90\x13\xdc\x4d\x86\x15\xcb\x30\x87\xe\xc0\x34\x91\x79\xe7\x5b\xe4\x24\xdc\x50\x9d\xf\xdc\x46\xe4\x24\xb7\x76\xac\x37";

#include <stdio.h>

int checker(const char * input){
    for(int i = 0; i < sizeof(enc_flag) - 1; i++){
        char byte = key[i % (sizeof(key)-1)] ^ input[i];
        if (byte != enc_flag[i])
            return 0;
    }
    return 1;
}

int main(){
    char input[100];
    puts("Tell me where you think the keys are and I'll let you know if thats right");
    fgets(input, 100, stdin);
    if(checker(input))
        puts("Yes, that is correct.");
    else
        puts("No, that is not correct.");
    return 0;
}
