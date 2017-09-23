import random
import sys

class UP: pass
class DOWN: pass
class RIGHT: pass
class LEFT: pass

directions = [ UP, DOWN, RIGHT, LEFT ]

def getRandomDirection():
    return random.choice(directions)

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

    def position(self):
        return (self.x, self.y)

    def adjascentTiles(self):
        m = self.maze
        x = self.x
        y = self.y

        l = [ m.getTile( x - 1, y ), m.getTile( x + 1, y ), m.getTile( x, y - 1 ), m.getTile( x, y + 1 ) ]
        return [ t for t in l if not( t is None ) ]

    def adjascent(self, direction):
       m = self.maze
       x = self.x
       y = self.y

       l = [ m.getTile( x - 1, y ), m.getTile( x + 1, y ), m.getTile( x, y - 1 ), m.getTile( x, y + 1 ) ]
       dirs = { UP: 0, DOWN: 1, LEFT: 2, RIGHT: 3 }

       return l[dirs[direction]]



    def drawTile(self):
        def draw(b):
            if(b):
                return ' '
            else:
                return '#'

        line1 = '#' + draw(self.up) + '#'
        line3 = '#' + draw(self.down) + '#'

        _all = self.up or self.down or self.left or self.right

        line2 = draw(self.left) + draw( _all ) + draw(self.right )

        return ( line1, line2, line3 )

    def connect(self, pos):

        if( pos == UP ):
            tNeig = self.maze.getTile(self.x - 1, self.y)
            self.up = True

            if( tNeig is None ):
                return None

            tNeig.down = True
        elif(pos == DOWN):
            tNeig = self.maze.getTile(self.x + 1, self.y)
            self.down = True

            if( tNeig is None ):
                return None

            tNeig.up = True
        elif(pos == RIGHT):
            tNeig = self.maze.getTile(self.x, self.y + 1)
            self.right = True

            if( tNeig is None ):
                return None

            tNeig.left = True
        elif(pos == LEFT):
            tNeig = self.maze.getTile(self.x, self.y - 1)
            self.left = True

            if( tNeig is None ):
                return None

            tNeig.right = True
        else:
            return None

        return tNeig

class Maze:

    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.initTiles()

    def initTiles(self):
        self.tiles = [[Tile(x, y, self) for y in range(0, self.w)] for x in range(0, self.h) ]

    def getTile(self, x, y = None ):

        if( y is None ):
            posX = x[0]
            posY = x[1]
        else:
            posX = x
            posY = y

        return self._getTile(posX, posY)


    def _getTile(self, x, y):

        if( x < 0 or x >= self.h or y < 0 or y >= self.w ):
            return None

        return self.tiles[x][y]

    def display(self):

        for row in self.tiles:
            line1 = ""
            line2 = ""
            line3 = ""
            for tile in row:
                t = tile.drawTile()
                line1 = line1 + t[0]
                line2 = line2 + t[1]
                line3 = line3 + t[2]

            print(line1)
            print(line2)
            print(line3)

def dfs( m ):
    pos = (0, 0)
    target = ( m.h - 1, m.w - 1 )
    visited = set()

    dfs_( m, pos, target, visited )

    m.getTile(pos).connect(LEFT)
    m.getTile(target).connect(RIGHT)


def dfs_( m, pos, target, visited ):


    if( target == pos ):
        return

    visited.add(pos)

    tile = m.getTile(pos)
    dirs = [ UP, DOWN, RIGHT, LEFT ]
    random.shuffle( dirs )

    for direction in dirs:
        nextT = tile.adjascent(direction)

        if( not (nextT is None) ):
            nextPos = nextT.position()
            if( not( nextPos in visited ) ):
                tile.connect(direction)
                dfs_( m, nextPos, target, visited )


width = int(sys.argv[1])
height = int(sys.argv[2])

maze = Maze(width, height)

dfs( maze )
maze.display()
