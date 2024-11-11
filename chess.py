# Chess game

class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def chek_move(self, x, y):
        result = False
        pass
        return result


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.x = x
        self.y = y

    def check_move(self, x, y):
        result = False
        pass
        return result


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.x = x
        self.y = y

    def check_move(self, x, y):
        result = False
        pass
        return result


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.x = x
        self.y = y

    def check_move(selfv):
        result = False
        pass
        return result


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.x = x
        self.y = y

    def check_move(self, x, y):
        result = False
        pass
        return result


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.x = x
        self.y = y

    def check_move(self, x, y):
        result = False
        pass
        return result


class Board():
    def __init__(self):
        self.Pieces = []

    def place_piece(self, piece, x, y):  # Place a piece on the board at a given position
        piece.x = x
        piece.y = y
        self.Pieces.append(piece)

    def move_piece(self, piece, xmov, ymov):  # Move a piece from one position to another
        piece.x += xmov
        piece.y += ymov

    def remove_piece(self, piece, x, y):  # Remove a piece from the board
        piece.x = -1
        piece.y = -1

    def get_piece_at_position(self, x, y):  # Return the piece at a given position
        for p in self.Pieces:
            if p.x == x and p.y == y:
                return (p)

    def get_all_pieces(self):  # Return a list of all the pieces on the board
        return self.Pieces

    def is_valid_move(self, piece, newx, newy):  # Check if a move is valid for a given piece
        return piece.check_move(self, piece, newx, newy)


## Testing objects

b = Board()
p1 = Pawn('W', 0, 1)
p2 = Pawn('W', 1, 1)
p3 = Pawn('W', 2, 1)
k1 = Knight('B', 3, 7)

# Place pieces on Board
b.place_piece(p1, 4, 1)
b.place_piece(p2, 5, 1)
b.place_piece(p3, 6, 1)
b.place_piece(k1, 4, 1)

print('Pieces on Board:')
for pp in b.get_all_pieces():
    print(f'{pp.__class__.__name__}, {pp.color} at {pp.x},{pp.y}')

print('\nWho on 5,1 :')

p = b.get_piece_at_position(5, 1)
print(f'{p.__class__.__name__}, {p.color} at {p.x},{p.y}')


