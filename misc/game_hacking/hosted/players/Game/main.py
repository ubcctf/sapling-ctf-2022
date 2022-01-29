#!/usr/bin/env python
from sys import argv
from Game import Game, GameOver, Win
from Flag import printFlags
import pygame
import os

if len(argv) <= 1 or argv[1] not in ["game", "replay", "check"]:
  print("./main.py <mode>")
  print("possible modes: game, replay, check")
  exit(1)

if os.path.basename(os.getcwd()) != "Game":
  print("Error: You must run the game from the Game/ folder")
  exit(1)

mode = argv[1]
game = Game(mode)

while True:
  try:
    game.tick()
  except Win:
    print("win!")
    if mode == "check":
      printFlags(game.getCompletionTime())
    break
  except GameOver:
    print("game over")
    break
  except:
    raise

if mode == "game":
  pygame.quit()
  filename = "./replay.txt"
  game.writeReplayFile(filename)
  print(f"Wrote replay input to {filename}")