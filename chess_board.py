# chess board
import objects.chess_piece as chess_piece
from objects.colours import Color
import copy

class Game:
    def __init__(self):
        self.plays = []
        self.play = 0
        self.plays.append(ChessBoard())

    def __str__(self):
        return str(self.plays[self.play])

class Tile:   
    def create_toggle_array(length=64):
        """
        Creates an array of specified length with a
        toggling pattern of 0s and 1s.
        Skips toggling on every 8th element.

        Args:
            length (int): The length of the array to be created. Default is 64.

        Returns:
            list: A list containing the toggling pattern of 0s and 1s.
        """
        array = []
        toggle = 0
        for i in range(length):
            if (i + 1) % 8 == 0:
                array.append(toggle)
            else:
                array.append(toggle)
                toggle = 1 - toggle
        return array

    _id = 0
    _cols = [ Color.LIGHT_TILE.value, Color.DARK_TILE.value ]
    _col_index_array = create_toggle_array()

    def __init__(self,x,y):
        self.id = Tile._id
        self.x = x
        self.y = y

        self.escape_col = Tile._cols[Tile._col_index_array[ self.id ]]
        Tile._id += 1

    def __str__(self):
        return f"Tile {self.id}"

    def __repr__(self):
        # return current location, list of all past locations
        return f"{self.__class__.__name__}{self.id}({self.x},{self.y})"  


    def show(self):
        coords = f"{self.x},{self.y}"
        txt= f"{self.escape_col}{coords.rjust(4)}{Color.RESET.value}"
        return f"{self.escape_col}{txt}{Color.RESET.value}"


class ChessBoard:
    def __init__(self):
        # create 8x8 board of TILE objects
        self.empty_board = [[Tile(x,y) for x in range(8)] for y in range(8)]
        self.board = copy.deepcopy(self.empty_board)
        

    def update_squares(self):
        # tell each piece where it is on the board
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if not isinstance(piece, Tile):
                    piece.store_piece_position(i, j)

    def reset_board(self):
        # populate the board with all the pieces in their initial positions
        for i in range(8):
            self.board[1][i] = chess_piece.BlackPawn(i+1)
            self.board[6][i] = chess_piece.WhitePawn(i+1)
        self.board[0][0] = chess_piece.BlackCastle(1)
        self.board[0][7] = chess_piece.BlackCastle(2)
        self.board[7][0] = chess_piece.WhiteCastle(1)
        self.board[7][7] = chess_piece.WhiteCastle(2)
        self.board[0][1] = chess_piece.BlackKnight(1)
        self.board[0][6] = chess_piece.BlackKnight(2)
        self.board[7][1] = chess_piece.WhiteKnight(1)
        self.board[7][6] = chess_piece.WhiteKnight(2)
        self.board[0][2] = chess_piece.BlackBishop(1)
        self.board[0][5] = chess_piece.BlackBishop(2)
        self.board[7][2] = chess_piece.WhiteBishop(1)
        self.board[7][5] = chess_piece.WhiteBishop(2)
        self.board[0][3] = chess_piece.BlackQueen()
        self.board[0][4] = chess_piece.BlackKing()
        self.board[7][3] = chess_piece.WhiteQueen()
        self.board[7][4] = chess_piece.WhiteKing()
        self.update_squares()

    def __str__(self):
        result = ''
        for row in self.board:
            for cell in row:
                if cell is None:
                    result += '.'
                else:
                    result += cell.show()
            result += '\n'
        return result

    def get_piece(self, piece_id: str):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece.id == piece_id:
                    return piece
        raise ValueError(f"No piece with id {piece_id}")


    def move_piece(self, piece_id: str, x: int, y: int ):
        # find the piece with the given id
        piece = self.get_piece(piece_id)
        piece.move(x, y)
        self.update_squares()