# Check out `CTF Adventure Land.pdf` for the latest challenge descriptions!
<s>
# MAPLE BACON CTF ADVENTURE LAND 1
## Points: 50

Maple has been teleported to CTF ADVENTURE LAND, a place with many dangers but also plenty of treasures.

Can you help Maple explore the world and obtain all of the flags?

For this challenge, the mischievous creatures have left behind a message for Maple on the wall. Can you find it?

Please submit a flag following the regex `maple{[a-zA-Z0-9_!\-\?]+}`. You do NOT need ```replay.txt``` for the first challenge in the series.

The recommended progression order for the MAPLE BACON CTF ADVENTURE LAND challenge series would be to clear challenges 1 and 2 first, as later challenges require you to speedrun the game. If you are stuck on the first challenge, feel free to start on the second one. The first one is NOT necessary to obtain the second flag.

## Game controls:
- Arrow keys to move
- Space bar to attack
- Game controls and more information are included in the readme.txt provided

## To run the game:
- Please ensure your version of Python is 3.6 or higher.
- In the `players/` directory, run:
  - `pip install --upgrade pip`
  - `pip install --user -r requirements.txt`
     - Installs the required dependencies for the game to run!
  - `cd Game/`
    - Change the working directory to be the `Game` folder! (Game must be run from this directory)
  - `python main.py`
    - Prints the different modes of the game!
      - `game`: Launches the game! You only need this mode to find and submit flag #1.
      - `replay`: Watch the replay of your `replay.txt`. You will need this for flag #2 and beyond.
      - `check`: Checks your solution to the challenge locally. You will need this for flag #2 and beyond.
    - e.g., to run the game, run `python main.py game`
- NOTE: the game needs to be run from an environment that supports graphical interfaces. E.g., the game can't run in WSL (Windows Subsystem for Linux) if it doesn't support GUI apps.

All flags for this series of challenges are in the standard format: `maple{[a-zA-Z0-9_!\-\?]+}`. For challenge 2-5, if your submitted solution to the server (refer to instructions in challenge 2) matches the requirements of the challenge, our server will print out a flag for you to submit with the corresponding challenge number.

# MAPLE BACON CTF ADVENTURE LAND 2
## Points: 50
Maple lost all their precious flags while searching for the important message! The creatures have hidden the flags around their land. Can you recover them?

NOTE:
- The moves you make during the game will be saved to `players/Game/replay.txt`.
- From this challenge onwards, you'll need to submit your `replay.txt` file to our server for verification.
- Linux/Mac users can use the command `cat replay.txt | nc ???<IP ADDRESS>?? ??PORT??`
- Windows users can use `cat replay.txt | telnet ???<IP ADDRESS>?? ??PORT??`
  - this requires that you enable the `telnet` client. 
  ```
  Control Panel -> Programs and Features -> Turn Windows Features on or off -> Telnet Client
  ```
- before submitting to the server, you can check your solution locally with `python main.py check`, this is the command we use on the server side. E.g., on Linux/Mac `cat replay.txt | python main.py check`
- **After the server verifies your solution, if it matches the requirement of the challenge, a flag (or multiple flags) will be printed for you to submit on the MapleCTF website. There should be a flag number along with the flag so you know where to submit it to.**

# MAPLE BACON CTF ADVENTURE LAND RACING 3
## Points: 150
Time is of utmost importance!

Note: After the server verifies your solution, if it matches the requirement of the challenge, a flag (or multiple flags) will be printed for you to submit on the MapleCTF website. There should be a flag number along with the flag so you know where to submit it to.

# MAPLE BACON CTF ADVENTURE LAND RACING 4
## Points: 300
It's time to start breaking the rules, we need those flags quick!

Note: After the server verifies your solution, if it matches the requirement of the challenge, a flag (or multiple flags) will be printed for you to submit on the MapleCTF website. There should be a flag number along with the flag so you know where to submit it to.

# MAPLE BACON CTF ADVENTURE LAND RACING 5
## Points: 300
???

Note: After the server verifies your solution, if it matches the requirement of the challenge, a flag (or multiple flags) will be printed for you to submit on the MapleCTF website. There should be a flag number along with the flag so you know where to submit it to.
  </s>
