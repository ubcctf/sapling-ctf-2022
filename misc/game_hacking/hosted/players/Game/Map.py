from collections import defaultdict
import pygame
from Renderer import Renderer

from math import floor, ceil

from Tile import TILE_LENGTH, Tile, colorTotileId, getTileIdToTileMap


class Map(pygame.sprite.Sprite):
  def __init__(self, renderer, mode, game):
    super(Map, self).__init__()
    self.game = game
    self.renderer = renderer
    self.mode = mode
    self.tileIdToTile = getTileIdToTileMap(self.mode)
    self.tileIdToTileCoords = defaultdict(set)
    self.loadMap()
    renderer.sprites.add(self)

  def loadMap(self):
    from PIL import Image
    im = Image.open("map.png")
    pixels = list(im.getdata())
    width, height = im.size
    self.map = [pixels[i*width:(i+1)*width] for i in range(height)]

    for i, line in enumerate(self.map):
      for j, color in enumerate(line):
        tile = self.tileIdToTile[colorTotileId[tuple(color)]]
        self.map[i][j] = tile
        self.tileIdToTileCoords[tile.id].add((j,i))

  def getPlayerSpawnPos(self, level):
    cc = self.tileIdToTileCoords[Tile.playerSpawnIds[level]]
    assert len(cc) == 1
    x, y = next(iter(cc))
    return (x * Tile.LENGTH + Tile.LENGTH / 2, (y + 1) * Tile.LENGTH)

  def getEnemyStartPos(self):
    result = []
    for y in range(len(self.map)):
      for x in range(len(self.map[0])):
        tile = self.map[y][x]
        if tile.isEnemySpawn:
          result.append((x * Tile.LENGTH + Tile.LENGTH / 2,
                         (y + 1) * Tile.LENGTH, tile.id))
    return result

  def render(self, display, cameraX, cameraY):
    xx = int(cameraX // Tile.LENGTH)
    yy = int(cameraY // Tile.LENGTH)

    for x in range(xx, xx+(Renderer.W // Tile.LENGTH)+1):
      for y in range(yy, yy+(Renderer.H // Tile.LENGTH)+1):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
          continue
        self.map[y][x].render(display, x, y, cameraX, cameraY)

  def getTile(self, x, y):
    if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
      return None
    return self.map[y][x]

  def setTile(self, x, y, id):
    if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
      return
    self.map[y][x] = self.tileIdToTile[id]

  def getCloseTileCollRects(self, rect, id):
    result = []
    for x in range(floor(rect.left/Tile.LENGTH) - 1,
                   ceil(rect.right/Tile.LENGTH) + 1):
      for y in range(floor(rect.top/Tile.LENGTH) - 1,
                     ceil(rect.bottom/Tile.LENGTH) + 1):
        if x >= 0 and y >= 0 and x < len(self.map[0]) and y < len(self.map):
          tile = self.map[y][x]
          if id == "solid" and tile.isSolid:
            result.append(tile.getCollRect().move(x*Tile.LENGTH, y*Tile.LENGTH))
          elif id == "spike" and tile.isSpike:
            result.append(tile.getDamageRect().move(x*Tile.LENGTH, y*Tile.LENGTH))
          elif (id == "orb" and tile.id == Tile.ORB) or (id == "flag" and tile.id == Tile.FLAG):
            result.append((tile.getCollRect().move(x*Tile.LENGTH, y*Tile.LENGTH), x, y))
    return result

  def getCloseSolidCollRects(self, rect):
    return self.getCloseTileCollRects(rect, "solid")

  def getCloseSpikeDamageRects(self, rect):
    return self.getCloseTileCollRects(rect, "spike")

  def getCloseOrbRects(self, rect):
    return self.getCloseTileCollRects(rect, "orb")

  def getCloseFlagRects(self, rect):
    return self.getCloseTileCollRects(rect, "flag")

  def triggerOrb(self, orbX, orbY):
    self.setTile(orbX, orbY, Tile.ORB_HOLDER_ON)
    self.renderer.addSfx(orbX * Tile.LENGTH, orbY * Tile.LENGTH,
                         "orb-holder-activate")

    # Don't deactivate spikes if another orb needs to be turned on nearby.
    for x in range(orbX - 3, orbX + 4):
      for y in range(orbY - 3, orbY + 4):
        tile = self.getTile(x, y)
        if tile is not None and tile.id == Tile.ORB_HOLDER_OFF:
          return

    # Search for the first spike.
    for x in range(orbX, orbX + 10):
      for y in range(orbY, orbY + 10):
        tile = self.getTile(x, y)
        if tile is not None and tile.id == Tile.ORB_SPIKE_U:
          self.eraseOrbSpikesAround(x, y)
          return

  def eraseOrbSpikesAround(self, spikeX, spikeY):
    x = spikeX
    while True:
      tile = self.getTile(x, spikeY)
      if tile is None:
        return
      if tile.id != Tile.ORB_SPIKE_U:
        return
      self.setTile(x, spikeY, Tile.EMPTY)
      self.renderer.addSfx(x * Tile.LENGTH, spikeY * Tile.LENGTH,
                           "orb-spike-off")
      x += 1

  def tick(self):
    pass