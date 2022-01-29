import os
import math
from Tile import tileToWorldCoords
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from Tux import Tux
from IE import IE
from Map import Map
from Renderer import Renderer
from Player import Player
from Tile import Tile
from Input import Input


def exit_with_msg(s):
  print(s)
  exit(1)


class GameOver(Exception):
  pass

class Win(Exception):
  pass

class Game(object):

  def __init__(self, mode):
    self.level = 0
    self.mode = mode
    self.numLevels = 3
    self.fps = 32
    replay = []
    if self.mode == "replay" or self.mode == "check":
      replay = self.loadReplay()
      if self.mode == "replay":
        print("replaying...")
      else:
        print("checking...")

    pygame.init()

    self.fpsClock = pygame.time.Clock()
    self.renderer = Renderer(self.mode, self)
    self.tickGroup = pygame.sprite.Group()
    self.playerGroup = pygame.sprite.Group()
    self.enemyGroup = pygame.sprite.Group()

    self.input = Input(self.mode, replay, self)
    self.map = Map(self.renderer, self.mode, self)
    self.spawnEntities()
    self.levelTransition = None
    self.won = False

  @property
  def player(self):
    for player in self.playerGroup:
      return player

  def loadReplay(self):
    replay = []
    print("Input replay file + empty line")
    for line in sys.stdin:
      line = line.strip()
      if len(line) == 0:
        break
      replay.append(int(line[:5], 2))
      max_length = 10_000
      if len(replay) > max_length:
        exit_with_msg(f"Input too long. Max length is {max_length}")
    if len(replay) == 0:
      exit_with_msg("Input empty")
    return replay

  def spawnEntities(self):
    self.spawnPlayer()
    for data in self.map.getEnemyStartPos():
      x, y, type = data
      if type == Tile.TUX_SPAWN:
        enemy = Tux(self.renderer, self.map, self.playerGroup, x, y)
      elif type == Tile.IE_SPAWN:
        enemy = IE(self.renderer, self.map, self.playerGroup, x, y)
      else:
        exit(1)
      self.tickGroup.add(enemy)
      self.enemyGroup.add(enemy)

  def spawnPlayer(self):
    x, y = self.map.getPlayerSpawnPos(self.level)
    player = Player(self, self.renderer, self.input, self.map, self.enemyGroup, x, y)
    self.tickGroup.add(player)
    self.playerGroup.add(player)

  def tick(self):
    if self.mode == "check":
      events = []
    else:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.locals.QUIT:
          raise GameOver

    self.input.tick(events)
    for sprite in self.tickGroup.sprites():
      sprite.tick()
    self.map.tick()

    if self.levelTransition:
      self.levelTransition.tick()
      if self.levelTransition.finished:
        self.levelTransition = None
        
    self.renderer.render()

    if self.mode != "check":
      self.fpsClock.tick(self.fps)

    if self.playerIsDead():
      self.spawnPlayer()

    if self.won and not self.player.isHoldingFlag:
      raise Win

    if self.reachedEndOfReplay():
      raise GameOver
  
  def gotFlag(self):

    if self.level == self.numLevels-1:
      self.won = True
      return
    
    self.levelTransition = LevelTransition(self)

  def playerIsDead(self):
    return len(self.playerGroup.sprites()) == 0

  def reachedEndOfReplay(self):
    return self.input.reachedEndOfReplay()

  def writeReplayFile(self, path):
    self.input.writeReplayFile(path)

  def getCompletionTime(self):
    return self.input.pos


class LevelTransition:

  teleportVectors = (
    (138-112, 104-139-1),
    (95-160, 110-111-1),
  )

  def __init__(self, game):
    self.game = game
    self.teleportVector = self.teleportVectors[self.game.level]
    self.ticks = 0
    self.finished = False
    self.alpha = 0

    if self.game.mode != "check":
      self.veil = pygame.Surface(pygame.display.get_surface().get_rect().size)
      self.veil.fill((0, 0, 0))

  def tick(self):

    nticks = 50
    if self.ticks < nticks:
      self.alpha = min(255, self.alpha + math.ceil(255/nticks))

    if self.ticks == 65:
      x, y = self.teleportVectors[self.game.level]
      self.game.player.x += tileToWorldCoords(x)
      self.game.player.y += tileToWorldCoords(y)
      self.game.level += 1

    ticksStart, ticksEnd = 70, 120
    if ticksStart <= self.ticks < ticksEnd:
      self.alpha = max(0, self.alpha - math.ceil(255/(ticksEnd - ticksStart)))
    
    self.ticks += 1

    if self.ticks == ticksEnd:
      self.finished = True

  def render(self, display):
    if self.alpha > 0:
      if self.game.mode != "check":
        self.veil.set_alpha(self.alpha)
        display.blit(self.veil, (0, 0))