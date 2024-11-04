from abc import ABC, abstractmethod
from typing import List
from objects.colours import Color

class Piece(ABC):
    # A Piece represents the most basic part of a Chess Piece
    # will have a colour White or Black
    def __init__(self, id: str):
        if id.upper().startswith('W'):
            self.escape_col = Color.WHITE.value
        elif id.upper().startswith('B'):
            self.escape_col = Color.BLACK.value
        else:
            raise ValueError('Piece ID must start with "W" or "B"')
        self.id = id
        self.reset_code = Color.RESET.value
        self.x = None
        self.y = None
        self.all_positions = list()  

    def store_piece_position(self, x, y):
        self.x = x
        self.y = y
        self.all_positions.append((x, y))

    def show_piece_position(self):
        return (self.x, self.y)

    def __repr__(self):
        # return current location, list of all past locations
        return f"{self.__class__.__name__}({self.id}, {self.show_piece_position()}) {self.all_positions}"  

    def show(self):
        """ Returns the piece ID with the appropriate color escape code. """
        txt = f"{self.id}"
        # pad txt with spaces on the left to make it 4 characters long
        return f"{self.escape_col}{txt.rjust(4)}{self.reset_code}"

        #return f"{self.escape_col}{self.id}{self.reset_code}"

    def move(self, x: int, y: int) -> None:
        """ 

        # check that the destination is not blocked when moving 2 spaces
        # check that the destination is not beyond the board
        # check that the destination is not occupied by another piece
        """
        print(f"Moving {self.id} from ({self.x},{self.y}) to ({x}, {y})")
        if y < 0 or y > 7:
            raise ValueError('Cannot move beyond the board')
        self.x = x
        self.y = y
        self.all_positions.append((self.x, self.y))


class Pawn(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in Pawn._ids:
            raise ValueError(f"Pawn with ID {id} already exists")
        # id must be with 1 .. 8 inc
        if not id[2].isdigit() or not (1 <= int(id[2]) <= 8):
            raise ValueError('Pawn ID must be in the range 1 to 8 inclusive')
        Pawn._ids.add(id)
        super().__init__(id)
        
class WhitePawn(Pawn):
    def __init__(self, id: int):
        self.id = f"WP{id}"
        super().__init__(self.id)



    def moveForward(self,spaces: int = 1) -> None:
        """ 
            Moves the pawn forward by the number of spaces specified. 
            Default is 1.
            White pawns move from bottom to top.
        """
        # check that the destination is not blocked when moving 2 spaces
        # check that the destination is not beyond the board
        # check that the destination is not occupied by another piece
        for i in range(spaces):
            newPostion = self.y - spaces
            if self.y - spaces < 0:
                raise ValueError('Cannot move beyond the board')
            if get_piece(self.x, self.y - spaces) in self.all_positions:
                raise ValueError('Cannot move to an occupied position')
  

        newPostion = self.y + spaces


        if self.y + spaces > 7:
            raise ValueError('Cannot move beyond the board')
        self.x -= spaces 
        self.all_positions.append((self.x, self.y))

        
class BlackPawn(Pawn):
    def __init__(self, id: int):
        self.id = f"BP{id}"
        super().__init__(self.id)

class Castle(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in Castle._ids:
            raise ValueError(f"Castle with ID {id} already exists")
        # id must be with 1 .. 2 inc
        if not id[2].isdigit() or not (1 <= int(id[2]) <= 2):
            raise ValueError('Castle ID must be in the range 1 to 2 inclusive')
        Castle._ids.add(id)
        super().__init__(id)
class WhiteCastle(Castle):
    def __init__(self, id: int):
        self.id = f"WC{id}"
        super().__init__(self.id)
class BlackCastle(Castle):
    def __init__(self, id: int):
        self.id = f"BC{id}"
        super().__init__(self.id)

class Knight(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in Knight._ids:
            raise ValueError(f"Knight with ID {id} already exists")
        # id must be with 1 .. 2 inc
        if not id[2].isdigit() or not (1 <= int(id[2]) <= 2):
            raise ValueError('Knight ID must be in the range 1 to 2 inclusive')
        Knight._ids.add(id)
        super().__init__(id)
class WhiteKnight(Knight):
    def __init__(self, id: int):
        self.id = f"WN{id}"
        super().__init__(self.id)
class BlackKnight(Knight):
    def __init__(self, id: int):
        self.id = f"BN{id}"
        super().__init__(self.id)

class Bishop(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in Bishop._ids:
            raise ValueError(f"Bishop with ID {id} already exists")
        # id must be with 1 .. 2 inc
        if not id[2].isdigit() or not (1 <= int(id[2]) <= 2):
            raise ValueError('Bishop ID must be in the range 1 to 2 inclusive')
        Bishop._ids.add(id)
        super().__init__(id)
class WhiteBishop(Bishop):
    def __init__(self, id: int):
        self.id = f"WB{id}"
        super().__init__(self.id)
class BlackBishop(Bishop):
    def __init__(self, id: int):
        self.id = f"BB{id}"
        super().__init__(self.id)

class Queen(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in Queen._ids:
            raise ValueError(f"Queen with ID {id} already exists")
        Queen._ids.add(id)
        super().__init__(id)
class WhiteQueen(Queen):
    def __init__(self):
        self.id = f"WQ"
        super().__init__(self.id)
class BlackQueen(Queen):
    def __init__(self):
        self.id = f"BQ"
        super().__init__(self.id)

class King(Piece):
    _ids = set()
    def __init__(self, id: str):
        if id in King._ids:
            raise ValueError(f"King with ID {id} already exists")
        King._ids.add(id)
        super().__init__(id)
class WhiteKing(King):
    def __init__(self):
        self.id = f"WK"
        super().__init__(self.id)
class BlackKing(King):
    def __init__(self):
        self.id = f"BK"
        super().__init__(self.id)



    