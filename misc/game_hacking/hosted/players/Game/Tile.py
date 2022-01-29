import pygame
from pygame import Rect


def tileToWorldCoords(x):
  return x*Tile.LENGTH


TILE_LENGTH = 32


class Tile:

  LENGTH = TILE_LENGTH
  SPIKE_LENGTH = 12

  EMPTY           = 0
  WALL            = 1
  SPIKE_U         = 2
  SPIKE_D         = 3
  SPIKE_L         = 4
  SPIKE_R         = 5
  ORB_SPIKE_U     = 6
  ORB_HOLDER_OFF  = 7
  ORB_HOLDER_ON   = 8
  ORB             = 9
  
  INVIS_WALL      = 15
  BACON_WALL      = 16

  PLAYER_SPAWN_1  = 20
  PLAYER_SPAWN_2  = 21
  PLAYER_SPAWN_3  = 22

  FLAG = 30

  TUX_SPAWN = 40
  IE_SPAWN  = 41

  playerSpawnIds = (
    PLAYER_SPAWN_1,
    PLAYER_SPAWN_2,
    PLAYER_SPAWN_3,
  )

  enemySpawnIds = (
    TUX_SPAWN,
    IE_SPAWN
  )

  def __init__(self, id, image, collRect=(0,0,TILE_LENGTH,TILE_LENGTH), damageRect=(0,0,TILE_LENGTH,TILE_LENGTH)):
    self.id = id
    self.collRect = collRect
    self.damageRect = damageRect
    self.image = image
    self.isSpike = id in (self.SPIKE_U, self.SPIKE_D, self.SPIKE_L, self.SPIKE_R, self.ORB_SPIKE_U)
    self.isOrbHolder = id in (self.ORB_HOLDER_OFF, self.ORB_HOLDER_ON)
    self.isEnemySpawn = id in self.enemySpawnIds
    self.isSolid = id == Tile.WALL or self.isOrbHolder or self.isSpike or id == Tile.INVIS_WALL

  def render(self, display, x, y, cameraX, cameraY):
    xx, yy = x*Tile.LENGTH-cameraX, y*Tile.LENGTH-cameraY
    if self.image:
      display.blit(self.image, (xx, yy))

  def getDamageRect(self):
    return Rect(*self.damageRect)

  def getCollRect(self):
    return Rect(*self.collRect)


def getTileIdToImageMap():

  tileIdToTileSetPosition = {}
  tileIdToTileSetPosition[Tile.WALL]            = (1, 0)
  tileIdToTileSetPosition[Tile.ORB_SPIKE_U]     = (0, 1)
  tileIdToTileSetPosition[Tile.SPIKE_U]         = (2, 0)
  tileIdToTileSetPosition[Tile.SPIKE_D]         = (3, 0)
  tileIdToTileSetPosition[Tile.SPIKE_L]         = (4, 0)
  tileIdToTileSetPosition[Tile.SPIKE_R]         = (5, 0)
  tileIdToTileSetPosition[Tile.ORB_HOLDER_OFF]  = (3, 1)
  tileIdToTileSetPosition[Tile.ORB_HOLDER_ON]   = (4, 1)
  tileIdToTileSetPosition[Tile.ORB]             = (5, 1)
  tileIdToTileSetPosition[Tile.FLAG]            = (0, 2)
  tileIdToTileSetPosition[Tile.INVIS_WALL]      = (3, 2)
  tileIdToTileSetPosition[Tile.BACON_WALL]      = (4, 2)

  tileIdToImage = {}

  tileset_image = pygame.image.load("Graphics/tileset.png").convert_alpha()
  if (tileset_image.get_width() % Tile.LENGTH != 0 or tileset_image.get_height() % Tile.LENGTH != 0):
    assert 0, "tileset wrong dimensions"

  for tileId, (x, y) in tileIdToTileSetPosition.items():
    tileIdToImage[tileId] = tileset_image.subsurface((x*Tile.LENGTH, y*Tile.LENGTH, Tile.LENGTH, Tile.LENGTH))
  
  return tileIdToImage


def getTileIdToTileMap(mode):

  tiles = {}

  if mode == "check":
    tileIdToImage = {}
  else:
    tileIdToImage = getTileIdToImageMap()

  def buildTile(tileId, *args, **kwargs):
    tiles[tileId] = Tile(id=tileId, image=tileIdToImage.get(tileId), *args, **kwargs)

  buildTile(Tile.EMPTY)
  buildTile(Tile.WALL)
  buildTile(Tile.ORB_SPIKE_U,    collRect=(0, Tile.LENGTH - Tile.SPIKE_LENGTH, Tile.LENGTH, Tile.SPIKE_LENGTH), damageRect=(1, Tile.LENGTH-Tile.SPIKE_LENGTH-1, Tile.LENGTH-2, 1))
  buildTile(Tile.SPIKE_U,        collRect=(0, Tile.LENGTH - Tile.SPIKE_LENGTH, Tile.LENGTH, Tile.SPIKE_LENGTH), damageRect=(1, Tile.LENGTH-Tile.SPIKE_LENGTH-1, Tile.LENGTH-2, 1))
  buildTile(Tile.SPIKE_D,        collRect=(0, 0, Tile.LENGTH, Tile.SPIKE_LENGTH),                               damageRect=(1, Tile.SPIKE_LENGTH+1, Tile.LENGTH-2, 1))
  buildTile(Tile.SPIKE_L,        collRect=(Tile.LENGTH - Tile.SPIKE_LENGTH, 0, Tile.SPIKE_LENGTH, Tile.LENGTH), damageRect=(Tile.LENGTH-Tile.SPIKE_LENGTH-1, 1, 1, Tile.LENGTH-2))
  buildTile(Tile.SPIKE_R,        collRect=(0, 0, Tile.SPIKE_LENGTH, Tile.LENGTH),                               damageRect=(Tile.SPIKE_LENGTH+1, 1, 1, Tile.LENGTH-2))
  buildTile(Tile.ORB_HOLDER_OFF, collRect=(10, 22, 12, 10))
  buildTile(Tile.ORB_HOLDER_ON,  collRect=(10, 22, 12, 10))
  buildTile(Tile.ORB,            collRect=(10, 21, 11, 11))
  buildTile(Tile.TUX_SPAWN)
  buildTile(Tile.IE_SPAWN)
  buildTile(Tile.FLAG, collRect=(13, 18, 11, 14))
  buildTile(Tile.PLAYER_SPAWN_1)
  buildTile(Tile.PLAYER_SPAWN_2)
  buildTile(Tile.PLAYER_SPAWN_3)
  buildTile(Tile.INVIS_WALL)
  buildTile(Tile.BACON_WALL)

  return tiles


colorTotileId = {
  (255,255,255):    Tile.EMPTY,
  (254,254,254):    Tile.INVIS_WALL,
  (145,50,0):       Tile.BACON_WALL,
  (0,0,0):          Tile.WALL,
  (0xc6,0x81,0x36): Tile.SPIKE_U,
  (0xc6,0x81,0x39): Tile.SPIKE_D,
  (0xc6,0x81,0x38): Tile.SPIKE_L,
  (0xc6,0x81,0x37): Tile.SPIKE_R,
  (0xff,0x81,0x36): Tile.ORB_SPIKE_U,
  (0x1f,0x77,0x00): Tile.ORB_HOLDER_OFF,
  (0x42,0xff,0x00): Tile.ORB,
  (0,0,255):        Tile.FLAG,
  (0xff,0xf0,0x00): Tile.TUX_SPAWN,
  (0x00,0xe7,0xff): Tile.IE_SPAWN,
  (255,0,0):        Tile.PLAYER_SPAWN_1,
  (254,0,0):        Tile.PLAYER_SPAWN_2,
  (253,0,0):        Tile.PLAYER_SPAWN_3,
}
