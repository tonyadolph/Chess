import sys

import objects.chess_piece as chess_piece
import objects.chess_board as chess_board


if __name__ == '__main__':

    # pawn1 = chess_piece.Pawn('WP1')
    # print(pawn1)
    # pawn2 = chess_piece.Pawn('BP1')
    # print(pawn2)

    # pawn3 = chess_piece.WhitePawn(3)
    # print(pawn3)

    # pawn4 = chess_piece.WhitePawn(4)
    # print(pawn4)
    # print(pawn4.show())
    # pawn5 = chess_piece.BlackPawn(4)
    # print(pawn5)
    # print(pawn5.show())

    # tile1   = chess_piece.Tile()
    # print(tile1)
    # print(tile1.show())
    # tile2  = chess_piece.Tile()
    # print(tile2)
    # print(tile2.show())
    
    
    board = chess_board.ChessBoard()
    print(board)

    #print(board.empty_board)
    board.reset_board()

    print(board)

    # print(board.board[0][0])

    # print(board.board[3][3])

    # board.move_piece(3,1,3,3)
    # print(board)

    # board.move_piece(3,6,3,4)
    # print(board)
    
    p = board.move_piece('WP4', 3, 4)   
    print(p)
    print(board)

    print(p)


    # TO DO
    """

    fix x - y coordinates

    add functions to move_piece,
    e.g. move_piece('WP4', 'forward1')
    e.g. move_piece('WP4', 'forward2')
    e.g. move_piece('WP4', 'diag_left')
    e.g. move_piece('WP4', 'diag_right')
    e.g. move_piece('WP4', piece_id)


    add functions to move_piece,


    """

    