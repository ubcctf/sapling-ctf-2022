#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>

#define ENDX 7
#define ENDY 0
#define ENDZ 7

#define STARTX 7
#define STARTY 1
#define STARTZ 0

#define DIM 8

unsigned char maze[] = {9, 20, 1, 16, 9, 5, 1, 1, 19, 1, 3, 1, 3, 18, 11, 7, 11, 14, 22, 18, 2, 16, 3, 18, 18, 8, 12, 12, 28, 20, 3, 16, 24, 12, 12, 20, 16, 9, 14, 21, 17, 16, 8, 12, 12, 7, 17, 18, 2, 16, 16, 8, 21, 2, 10, 5, 16, 8, 20, 16, 2, 8, 20, 2, 17, 48, 1, 40, 12, 5, 8, 21, 42, 20, 18, 1, 1, 42, 21, 19, 8, 21, 57, 38, 10, 37, 27, 38, 32, 10, 23, 1, 48, 43, 15, 36, 32, 8, 31, 47, 44, 23, 3, 48, 33, 40, 6, 2, 8, 6, 51, 32, 10, 53, 40, 5, 40, 12, 15, 4, 40, 6, 40, 46, 28, 4, 58, 4, 32, 32, 25, 5, 8, 28, 5, 48, 17, 32, 50, 2, 8, 5, 50, 32, 11, 36, 56, 4, 1, 10, 45, 4, 2, 25, 52, 1, 50, 17, 26, 4, 8, 6, 41, 30, 4, 34, 8, 36, 16, 9, 30, 20, 8, 13, 60, 5, 25, 55, 8, 12, 12, 6, 17, 18, 2, 2, 8, 12, 44, 28, 62, 20, 16, 16, 32, 8, 29, 37, 1, 33, 49, 8, 37, 16, 2, 2, 51, 3, 19, 8, 62, 20, 16, 16, 18, 2, 2, 32, 41, 4, 33, 48, 40, 4, 24, 12, 22, 32, 2, 9, 28, 4, 40, 12, 52, 48, 24, 30, 44, 4, 32, 56, 5, 1, 1, 1, 32, 48, 16, 8, 14, 22, 26, 54, 48, 32, 33, 40, 13, 4, 32, 24, 13, 4, 34, 8, 7, 33, 17, 24, 54, 1, 32, 8, 55, 42, 63, 36, 40, 7, 17, 1, 26, 20, 2, 32, 17, 3, 34, 10, 36, 8, 28, 5, 51, 18, 16, 17, 33, 48, 48, 34, 26, 4, 8, 39, 10, 12, 4, 8, 20, 33, 56, 6, 24, 36, 32, 48, 48, 2, 1, 25, 28, 4, 16, 32, 25, 4, 18, 27, 12, 4, 32, 32, 42, 4, 8, 15, 60, 20, 56, 4, 25, 20, 48, 2, 48, 48, 1, 16, 58, 4, 8, 5, 1, 1, 58, 20, 48, 32, 41, 63, 7, 34, 48, 17, 40, 20, 18, 3, 10, 5, 16, 26, 53, 1, 32, 2, 32, 10, 20, 32, 58, 22, 9, 52, 33, 1, 41, 20, 32, 17, 34, 48, 2, 18, 26, 13, 28, 22, 8, 12, 36, 48, 32, 2, 48, 32, 48, 8, 53, 40, 28, 52, 40, 4, 8, 12, 6, 16, 32, 32, 32, 1, 16, 57, 29, 4, 32, 56, 20, 51, 32, 19, 26, 12, 36, 32, 48, 2, 8, 22, 16, 8, 60, 4, 48, 32, 1, 32, 8, 13, 4, 32, 1, 32, 11, 37, 8, 47, 44, 4, 34, 32, 2, 3, 1, 43, 4, 8, 45, 4, 32, 2, 34, 3, 33, 32, 10, 4, 1, 1, 8, 38, 10, 4, 1, 1, 43, 38, 40, 12, 4, 32, 34, 35, 2, 32, 41, 4, 8, 12, 36, 3, 8, 36, 42, 4, 40, 4, 32, 2};

int curx = STARTX;
int cury = STARTY;
int curz = STARTZ;

unsigned char iv[] = {'0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5'};
unsigned char flag[] ={0xc6, 0x3d, 0x55, 0x7c, 0x57, 0x2e, 0xdd, 0xeb, 0x45, 0xf3, 0x2c, 0x7c, 0x83, 0xa5, 0x6d, 0x41, 0x3b, 0x5c, 0x31, 0x8e, 0x3d, 0xce, 0xa8, 0x0c, 0x4e, 0x53, 0x8e, 0xc2, 0x4d, 0x55, 0x90, 0x73};

static inline int maze_index(){
    return DIM*DIM*curz+DIM*cury+curx;
}

void fail(){
    ERR_print_errors_fp(stderr);
    puts("Nope! Bye!");
    exit(0);
}

int decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
            unsigned char *iv, unsigned char *plaintext)
{
    EVP_CIPHER_CTX *ctx;

    int len;

    int plaintext_len;

    /* Create and initialise the context */
    if(!(ctx = EVP_CIPHER_CTX_new()))
        fail();

    /*
     * Initialise the decryption operation. IMPORTANT - ensure you use a key
     * and IV size appropriate for your cipher
     * In this example we are using 256 bit AES (i.e. a 256 bit key). The
     * IV size for *most* modes is the same as the block size. For AES this
     * is 128 bits
     */
    if(1 != EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv))
        fail();

    /*
     * Provide the message to be decrypted, and obtain the plaintext output.
     * EVP_DecryptUpdate can be called multiple times if necessary.
     */
    if(1 != EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len))
        fail();
    plaintext_len = len;

    /*
     * Finalise the decryption. Further plaintext bytes may be written at
     * this stage.
     */
    if(1 != EVP_DecryptFinal_ex(ctx, plaintext + len, &len))
        fail();
    plaintext_len += len;

    /* Clean up */
    EVP_CIPHER_CTX_free(ctx);

    return plaintext_len;
}

int move(char move){

    // Check moves
    switch (move)
        {
        case 'w':
            if((maze[maze_index()] & 2) == 2)
                cury -= 1;
            break;
        case 'a':
            if((maze[maze_index()] & 4) == 4)
                curx -=1;
            break;
        case 's':
            if((maze[maze_index()] & 1) == 1)
                cury += 1;
            break;
        case 'd':
            if((maze[maze_index()] & 8) == 8)
                curx += 1;
            break;
        case 'q':
            if((maze[maze_index()] & 16) == 16)
                curz += 1;
            break;
        case 'e':
            if((maze[maze_index()] & 32) == 32)
                curz -= 1;
            break;
        default:
            return 0;
            break;
        }

        // Rollback if going out of bounds.
        if(curx<0)
            curx += 1;
        if(cury<0)
            cury +=1;
        if(curz<0)
            curz += 1;
        return 1;
}

int main(){
    char input[27];
    char *p = &input[0];
    char key[SHA256_DIGEST_LENGTH];
    char plaintext[128];
    int length;

    puts("Password please!");
    fgets(input, sizeof(input), stdin);

    while(*p){
        if(!move(*p))
            break;
        p++;
        if(curx == ENDX && cury == ENDY && curz == ENDZ){
            puts("Correct! Printing flag!");
            SHA256(input, 26, key);
            length = decrypt(flag, 32, key, iv, plaintext);
            plaintext[length] = 0;
            puts(plaintext);
            return 0;
        }
    }
    fail();
    return 0;
}