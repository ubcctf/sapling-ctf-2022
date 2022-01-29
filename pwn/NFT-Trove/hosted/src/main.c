/*
 * Copyright 2013, 2017, Jernej Kovacic
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software. If you wish to use our Amazon
 * FreeRTOS name, please do so in a fair use way that does not cause confusion.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */


/**
 * @file
 * A simple demo application.
 *
 * @author Jernej Kovacic
 */


#include <stddef.h>
#include <string.h>

#include <FreeRTOS.h>
#include <task.h>

#include "app_config.h"
#include "print.h"
#include "receive.h"

__attribute__((always_inline)) static inline void __WFI(void)
{
    taskENTER_CRITICAL();
    for(;;);
  /* __asm volatile ("wfi"); */
}

/*
 * This diagnostic pragma will suppress the -Wmain warning,
 * raised when main() does not return an int
 * (which is perfectly OK in bare metal programming!).
 *
 * More details about the GCC diagnostic pragmas:
 * https://gcc.gnu.org/onlinedocs/gcc/Diagnostic-Pragmas.html
 */
#pragma GCC diagnostic ignored "-Wmain"

void vApplicationIdleHook(void)
{
    vDirectPrintMsg("idle\n");
}

static void heapWrite(size_t n, char* data)
{
    void* dest;

    if (n == 0) {
        vDirectPrintMsg("Invalid size!\n");
        return;
    }
    dest = pvPortMalloc(n + 4);
    *((int*)dest) = 0xABADBABE; /* there are many worthless things out there, but this line is mine :3 */
    memcpy(dest + 4, data, n);
}

unsigned char HexChar (char c)
{
    if ('0' <= c && c <= '9') return (unsigned char)(c - '0');
    if ('A' <= c && c <= 'F') return (unsigned char)(c - 'A' + 10);
    if ('a' <= c && c <= 'f') return (unsigned char)(c - 'a' + 10);
    return 0xFF;
}

int hexToBin (const char* s, unsigned char * buff, int length)
{
    int result;
    if (!s || !buff || length <= 0) return -1;

    for (result = 0; *s; ++result)
    {
        unsigned char msn = HexChar(*s++);
        if (msn == 0xFF) return -1;
        unsigned char lsn = HexChar(*s++);
        if (lsn == 0xFF) return -1;
        unsigned char bin = (msn << 4) + lsn;

        if (length-- <= 0) return -1;
        *buff++ = bin;
    }
    return result;
}

char* hexToBytes(char* string) {

    if(string == NULL)
       return NULL;

    size_t slength = strlen(string);
    if((slength % 2) != 0) // must be even
       return NULL;

    size_t dlength = slength / 2;

    char* data = pvPortMalloc(dlength);
    memset(data, 0, dlength);

    size_t index = 0;
    while (index < slength) {
        char c = string[index];
        int value = 0;
        if(c >= '0' && c <= '9')
          value = (c - '0');
        else if (c >= 'A' && c <= 'F')
          value = (10 + (c - 'A'));
        else if (c >= 'a' && c <= 'f')
          value = (10 + (c - 'a'));
        else {
          vPortFree(data);
          return NULL;
        }

        data[(index/2)] += value << (((index + 1) % 2) * 4);

        index++;
    }

    return data;
}

int parseInt(char *str)
{
  int result;
  int puiss;

  result = 0;
  puiss = 1;
  while (('-' == (*str)) || ((*str) == '+'))
  {
      if (*str == '-')
        puiss = puiss * -1;
      str++;
  }
  while ((*str >= '0') && (*str <= '9'))
  {
      result = (result * 10) + ((*str) - '0');
      str++;
  }
  return (result * puiss);
}

char* recvLine(void)
{
    while (!recvReady) {
        vTaskDelay( 1000 / portTICK_RATE_MS );
    }
    recvReady = false;
    return recvBuf;
}

int recvInt()
{
    char* buf = recvLine();
    return parseInt(buf);
}

/* Task function - may be instantiated in multiple tasks */
void fillTrove( void* params )
{
    int n;
    char* data;
    char* byteData;

    (void) params;
    while (true) {
        vTaskDelay( 1000 / portTICK_RATE_MS );
        vDirectPrintMsg("How big is your NFT?\r\n");
        n = recvInt();
        if (n == 0) {
            vDirectPrintMsg("That's not legal! >:|\n");
            continue;
        }
        if (n > (RECV_BUFFER_LEN - 4)) {
            vDirectPrintMsg("Err, that's too big to bury...\n");
            continue;
        }
        vDirectPrintMsg("Place your NFT below:\n");
        data = recvLine();
        byteData = pvPortMalloc(strlen(data));
        hexToBin(data, (unsigned char*) byteData, strlen(data));

        heapWrite(n, byteData);
        vPortFree(byteData);
        vDirectPrintMsg("Your NFT has been buried successfully! :)\n");
        vDirectPrintMsg("Now on to the next one...\n");
    }

    /*
     * If the task implementation ever manages to break out of the
     * infinite loop above, it must be deleted before reaching the
     * end of the function!
     */
    vTaskDelete(NULL);
}

/*
 * A convenience function that is called when a FreeRTOS API call fails
 * and a program cannot continue. It prints a message (if provided) and
 * ends in an infinite loop.
 */
static void FreeRTOS_Error(const portCHAR* msg)
{
    if ( NULL != msg )
    {
        vDirectPrintMsg(msg);
    }

    for ( ; ; );
}

static void initialize(void)
{
    /* Init of print related tasks: */
    if ( pdFAIL == printInit(PRINT_UART_NR) )
    {
        FreeRTOS_Error("Initialization of print failed\r\n");
    }

    /* Init of receiver related tasks: */
    if ( pdFAIL == recvInit(RECV_UART_NR) )
    {
        FreeRTOS_Error("Initialization of receiver failed\r\n");
    }

    /* Create a print gate keeper task: */
    if ( pdPASS != xTaskCreate(printGateKeeperTask, "gk", 128, NULL,
                               PRIOR_PRINT_GATEKEEPR, NULL) )
    {
        FreeRTOS_Error("Could not create a print gate keeper task\r\n");
    }

    if ( pdPASS != xTaskCreate(recvTask, "recv", 1000, NULL, PRIOR_RECEIVER, NULL) )
    {
        FreeRTOS_Error("Could not create a receiver task\r\n");
    }
    vDirectPrintMsg("UART initialized.\n");
}

/* Startup function that creates and runs two FreeRTOS tasks */
void main(void)
{
    char* flag = "maple{y0u_c4nt_ju5t_g0_4nd_c0py_my_nft}";

    initialize();

    vDirectPrintMsg(" _   _ ______ _____   ___________ _____  _   _ _____\n");
    vDirectPrintMsg("| \\ | ||  ___|_   _| |_   _| ___ \\  _  || | | |  ___|\n");
    vDirectPrintMsg("|  \\| || |_    | |     | | | |_/ / | | || | | | |__\n");
    vDirectPrintMsg("| . ` ||  _|   | |     | | |    /| | | || | | |  __|\n");
    vDirectPrintMsg("| |\\  || |     | |     | | | |\\ \\\\ \\_/ /\\ \\_/ / |___\n");
    vDirectPrintMsg("\\_| \\_/\\_|     \\_/     \\_/ \\_| \\_|\\___/  \\___/\\____/\n\n\n\n");

    vDirectPrintMsg("Welcome to NFT Trove, our super-secure NFT Storage-as-a-service!\n");
    vDirectPrintMsg("Simply hand us your NFT and we'll keep it safe from copy theft.\n");
    vDirectPrintMsg("Guaranteed to keep your NFT in one piece forever! (or until this board resets)\r\n");

    vDirectPrintMsg("Our system's so secure that we even trust it with our own NFTs!\n");
    heapWrite(sizeof(flag), flag);

    if ( pdPASS != xTaskCreate(fillTrove, "task", 128, NULL,
                               PRIOR_PERIODIC, NULL) )
    {
        FreeRTOS_Error("Could not create task\r\n");
    }

    /* Start the FreeRTOS scheduler */
    vTaskStartScheduler();

    /*
     * If all goes well, vTaskStartScheduler should never return.
     * If it does return, typically not enough heap memory is reserved.
     */
    FreeRTOS_Error("Could not start the scheduler!!!\r\n");

    /* just in case if an infinite loop is somehow omitted in FreeRTOS_Error */
    for ( ; ; );
}
