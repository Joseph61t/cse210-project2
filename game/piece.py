import random

class Piece:
    def __init__(self) -> None:
        self.piece = {}
        self.rotation = 0
        self.set_piece()

    def set_piece(self):
        pieces = [
            # 'I' 
            [0, 1, 0, 0, 
                  0, 1, 0, 0,
                  0, 1, 0, 0,
                  0, 1, 0, 0], 
            # 'L' 
            [0, 2, 0, 0, 
                  0, 2, 0, 0,
                  0, 2, 2, 0, 
                  0, 0, 0, 0],
            # 'J' 
            [0, 0, 3, 0, 
                  0, 0, 3, 0,
                  0, 3, 3, 0, 
                  0, 0, 0, 0],
            # 'T' 
            [4, 4, 4, 0,
                  0, 4, 0, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
            # 'Z' 
            [5, 5, 0, 0,
                  0, 5, 5, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            # 'S' 
            [0, 6, 6, 0,
                  6, 6, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            # 'O' 
            [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]
        ]
        pieceList = list(pieces.items())
        self.piece.append(random.choice(pieceList))

    def set_rotation(self, key):
        rotation1 = {
            'I': [0, 1, 0, 0, 
                  0, 1, 0, 0,
                  0, 1, 0, 0,
                  0, 1, 0, 0], 
            'L': [0, 2, 0, 0, 
                  0, 2, 0, 0,
                  0, 2, 2, 0, 
                  0, 0, 0, 0],
            'J': [0, 0, 3, 0, 
                  0, 0, 3, 0,
                  0, 3, 3, 0, 
                  0, 0, 0, 0],
            'T': [4, 4, 4, 0,
                  0, 4, 0, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
            'Z': [5, 5, 0, 0,
                  0, 5, 5, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            'S': [0, 6, 6, 0,
                  6, 6, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            'O': [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]
            }
        rotation2 = {
            'I': [0, 0, 0, 0, 
                  0, 0, 0, 0,
                  1, 1, 1, 1,
                  0, 0, 0, 0], 
            'L': [0, 0, 0, 0, 
                  2, 2, 2, 0,
                  2, 0, 0, 0, 
                  0, 0, 0, 0],
            'J': [0, 0, 0, 0, 
                  3, 0, 0, 0,
                  3, 3, 3, 0, 
                  0, 0, 0, 0],
            'T': [0, 4, 0, 0,
                  4, 4, 0, 0,
                  0, 4, 0, 0, 
                  0, 0, 0, 0],
            'Z': [0, 5, 0, 0,
                  5, 5, 0, 0,
                  5, 0, 0, 0,
                  0, 0, 0, 0],
            'S': [6, 0, 0, 0,
                  6, 6, 0, 0,
                  0, 6, 0, 0,
                  0, 0, 0, 0],
            'O': [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]
            }        
        rotation3 = {
            'I': [0, 1, 0, 0, 
                  0, 1, 0, 0,
                  0, 1, 0, 0,
                  0, 1, 0, 0], 
            'L': [0, 2, 2, 0, 
                  0, 0, 2, 0,
                  0, 0, 2, 0, 
                  0, 0, 0, 0],
            'J': [0, 3, 3, 0, 
                  0, 3, 0, 0,
                  0, 3, 0, 0, 
                  0, 0, 0, 0],
            'T': [0, 4, 0, 0,
                  4, 4, 4, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
            'Z': [5, 5, 0, 0,
                  0, 5, 5, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            'S': [0, 6, 6, 0,
                  6, 6, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
            'O': [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]
            }
        rotation4 = {
            'I': [0, 0, 0, 0, 
                  0, 0, 0, 0,
                  1, 1, 1, 1,
                  0, 0, 0, 0], 
            'L': [0, 0, 0, 0, 
                  0, 0, 2, 0,
                  2, 2, 2, 0, 
                  0, 0, 0, 0],
            'J': [0, 0, 0, 0, 
                  3, 3, 3, 0,
                  0, 0, 3, 0, 
                  0, 0, 0, 0],
            'T': [0, 4, 0, 0,
                  0, 4, 4, 0,
                  0, 4, 0, 0, 
                  0, 0, 0, 0],
            'Z': [0, 5, 0, 0,
                  5, 5, 0, 0,
                  5, 0, 0, 0,
                  0, 0, 0, 0],
            'S': [6, 0, 0, 0,
                  6, 6, 0, 0,
                  0, 6, 0, 0,
                  0, 0, 0, 0],
            'O': [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]
            }
        
        if key == "#":
            if self.rotation < 4:
               self.rotation += 1
            else:
                self.rotation = 1
        elif key == "@":
            if self.rotation > 1:
                self.rotation -= 1
            else:
                self.rotation = 4
        else:
            pass
        
        if self.rotation == 1:
            self.piece[1] = rotation1[self.piece[0]]
        elif self.rotation == 2:
            self.piece[1] = rotation2[self.piece[0]]
        elif self.rotation == 3:
            self.piece[1] = rotation3[self.piece[0]]
        else:
            self.piece[1] = rotation4[self.piece[0]]

piece = Piece()
print(piece.piece)
piece.set_rotation('@')
print(piece.piece)