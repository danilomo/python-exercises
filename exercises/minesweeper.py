import sys
import random



def valid(x, size):
    return x >= 0 and x < size

class MineBoard:

    def __init__( self, mines, size ):
        self._mines = mines
        self._size = size

        self._getRandomMines()
        self._initBoard()
        self._visible = [[False for i in range(0, self._size)] for j in range(0, self._size) ]


    def play( self, i, j ):

        if( self._board[i][j] == -1 ):
            print("Kaboooom! You lose!")
        elif( self._board[i][j] == 0 ):
            self._reveal( i, j )
        else:
            self._visible[i][j] = True


    def _reveal( self, i, j ):

        if( not self._valid(i, j) ):
            return

        if( self._visible [i][j] ):
            return

        if( self._board [i][j] != 0 ):
            return


        self._visible[i][j] = True

        self._reveal( i - 1, j )
        self._reveal( i + 1, j )
        self._reveal( i, j - 1 )
        self._reveal( i, j + 1 )



    def printBoard(self):
        b = self._board

        for i in range(0, self._size):
            line = ""
            for j in range(0, self._size):
                val = b[i][j]

                if(val < 0):
                    val = '*'

                if(not self._visible[i][j]):
                    val = '#'

                line = line + str(val) + " "

            print(line)



    def _getRandomMines(self):

        l = []

        for i in range(0, self._mines):
            mI = random.randint(0, self._size - 1)
            mJ = random.randint(0, self._size - 1)

            l.append( (mI, mJ) )

        self._minesPos = l


    def _initBoard( self ):

        b = [ [0 for j in range(0, self._size)] for i in range(0, self._size) ]
        self._board = b

        for m in self._minesPos:
            self._setMine(m) 

        for m in self._minesPos:
            i = m[0]
            j = m[1]
            b[i][j] = -1


    def _setMine( self, m ):
        i = m[0]
        j = m[1]

        self._incrMine( i - 1, j - 1 )
        self._incrMine( i - 1, j )
        self._incrMine( i - 1, j + 1 )
        self._incrMine( i , j - 1 )
        self._incrMine( i , j + 1 )
        self._incrMine( i + 1, j - 1 )
        self._incrMine( i + 1, j )
        self._incrMine( i + 1, j + 1 )

    def _incrMine( self, i, j ):
        
        if( not self._valid(i, j) ):
            return

        self._board[i][j] = self._board[i][j] + 1

    def _valid( self, i, j ):
        return (valid(i, self._size) and valid(j, self._size)) 




class Game:

    def __init__( self, mines, size ):

        self._board = MineBoard( mines, size )

    def run( self ):

        self._board.printBoard()

        while(True):
            move = self._play()

            if( not(move is None) ):
                self._board.play( move[0], move[1] )
                self._board.printBoard()
            else:
                print("Invalid move.")

        

    def _play( self ):

        _input = input( "Your move: " )
        _input = _input.split()
        
        try:
            i = int(_input[0])
            j = int(_input[1])

            if(not self._board._valid(i, j)):
                return None

            return (i, j)
        except:
            return None

mines = int(sys.argv[1])
boardSize = int(sys.argv[2])



game = Game( mines, boardSize )
game.run()

