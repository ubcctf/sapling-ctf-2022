#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <errno.h>

void getFlag();
int overwrite(void *addr, int value);

unsigned long BASE_ADDR = 0x400000;
int PERMISSION_LEVEL = PROT_READ | PROT_WRITE | PROT_EXEC;
int FLAG_LENGTH = 0x20;

int main(int argc, char *argv[])
{
    int offset;
    int value;
    char buf[1];
    
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    printf("\nWhats the offset captain?\n>> ");
    scanf("%4x", &offset);

    printf("\nWhats the payload captain?\n>> ");
    scanf("%2x", &value);

    if (offset > 0x2000 || offset < 0x0)
    {
        printf("That target is out of range captain!\n");
        exit(1);
    }

    void *base_addr = (void *)BASE_ADDR + offset;

    if (overwrite(base_addr, value) == -1)
    {
        puts("\nAddress failed to be overwritten.");
        exit(1);
    }
    
    // Call print flag again
    printf("\nFetching flag now.\n");
    getFlag();

    return 0;
}

int overwrite(void *addr, int value)
{
    // update the page permissions
    int page_size = getpagesize();
    void* page = addr - (unsigned long)addr % page_size;

    if (mprotect(page, page_size, PERMISSION_LEVEL) == -1)
    {
        return -1;
    }

    // change something
    unsigned char *target = (unsigned char *)addr;
    *target = value;

    return 0;
}

void getFlag()
{
    char flag[FLAG_LENGTH];
    FILE *fd = fopen("flag.txt", "r");
    
    if (fd == NULL) {
        puts("\nEnsure there is a valid flag file.");
        exit(1);
    }

    fgets(flag, 32, fd);
    syscall(1,1,flag,FLAG_LENGTH);
    fclose(fd);
}