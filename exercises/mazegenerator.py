import random
import sys

class Tile:

    def __init__( self, x, y, maze ):
        self.x = x
        self.y = y
        self.maze = maze

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def __repr__(self):
        return str((self.x, self.y))

    def drawTile(self):
        def draw(b):
            if(b):
                return ' '
            else:
                return '#'

        line1 = '#' + draw(self.up) + '#'
        line3 = '#' + draw(self.down) + '#'

        _all = self.up or self.down or self.left or self.right

        line2 = draw(self.left) + draw( not _all ) + draw(self.right )

        return ( line1, line2, line3 )

class Maze:

    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.initTiles()

    def initTiles(self):

        self.tiles = [[Tile(x, y, self) for y in range(0, self.w)] for x in range(0, self.h) ]


width = int(sys.argv[1])
height = int(sys.argv[2])

maze = Maze(width, height)
