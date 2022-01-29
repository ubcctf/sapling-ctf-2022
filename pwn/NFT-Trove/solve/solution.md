# Solution

## Summary
Multiple interesting vulnerabilities and machine quirks culminate into what is an ARM shellcode problem with extra steps.

## Notes
- size of NFT checked as signed int so pass a value less than -4.
- value will be used as unsigned by malloc, which fails and returns 0.
- malloc is unchecked and value is used for write destination of memcpy.
- memcpy length ends up being a very large number, which would normally crash or timeout a regular program. However, overwriting the beginning region in memory triggers the reset vector, which then executes up to 1000 bytes that the user may have managed to write into the reset vector region.
- flag is somewhere in heap memory so write a shellcode that searches memory for something that looks like the flag, then writes that memory into UART0 of the ARM926EJ-S.
