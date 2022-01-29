You can run the emulated board locally in a docker container with `./start.sh`.

Connect to it with `nc 0.0.0.0 31337`.

The docker container installs `gdb-multiarch`, which you can use to debug the running emulated board by using `QEMU_DEBUG=1 ./start.sh` and then running
```
gdb-multiarch image.elf
target remote localhost:1234
```
to connect to the debugger attached to the emulated board.

Note the python scripts provided are only needed to interact with the emulator properly and are not a target.

There is a 120s timeout on any running server instances to avoid overuse and characters are sent in a delayed manner, so use your bytes wisely!
