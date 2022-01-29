# This is ONLY supposed to run on the server -- NOT to be included in the players/ directory

import main
import hashlib
from Input import KeysPressed

assert main.mode == "check"

# NOTE If player submits input that's too long, the program just exits and we don't log

replay = ""
for keys in main.game.input.replay:
    replay += "{0:05b}\n".format(KeysPressed(keys).asNumber())
replay += "\n"

hash = hashlib.md5(replay.encode("ascii")).hexdigest()
win = "win" if main.game.won else "lose"
filename = f"/usr/share/volume/{win}_{main.game.getCompletionTime()}-{hash}.replay"
with open(filename, "w") as f:
    f.write(replay)