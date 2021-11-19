import pygame

class Piece:
    def __init__(self, position, color, race, pic):
        self.position = position
        self.color = color
        self.race = race
        self.pic = pic
    
    # Returns the moves that could be made without minding check
    def legalMoves(self, board, enpassantable=None):
        legal_moves = []
        x = self.position[0]
        y = self.position[1]
        locations = [i.position for i in board]

        if self.race == 'P':
            if [[x, y+1], [x, y-1]][self.color] not in locations:
                legal_moves.append([[x, y+1], [x, y-1]][self.color])
                if y == [1, 6][self.color] and [[x, y+2], [x, y-2]][self.color] not in locations:
                    legal_moves.append([[x, y+2], [x, y-2]][self.color])
            if [[x+1, y+1], [x+1, y-1]][self.color] in locations:
                legal_moves.append([[x+1, y+1], [x+1, y-1]][self.color])
            if [[x-1, y+1], [x-1, y-1]][self.color] in locations:
                legal_moves.append([[x-1, y+1], [x-1, y-1]][self.color])

        if self.race == 'R' or self.race == 'Q':
            for i in [-1, 1]:
                j = 1
                legal_moves.append([x+i*j, y])
                while [x+i*j, y] not in [z.position for z in board] and -1 < x+i*j < 8 :
                    #no pieces at the given position
                    j+=1
                    legal_moves.append([x+i*j, y])
            for i in [-1, 1]:
                j = 1
                legal_moves.append([x, y+i*j])
                while [x, y+i*j] not in [z.position for z in board] and -1 < y+i*j < 8 :
                    #no pieces at the given position
                    j+=1
                    legal_moves.append([x, y+i*j])
            
        if self.race == 'N':
            for i, j in [[-2, -1], [2, -1], [-2, 1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]:
                legal_moves.append([x+i, y+j])

        if self.race == 'B' or self.race == 'Q':
            for i, k in [[1, 1], [-1, -1], [1, -1], [-1, 1]]:
                j = 1
                legal_moves.append([x+i*j, y+k*j])
                while [x+i*j, y+k*j] not in [z.position for z in board] and -1 < x+i*j < 8 and -1 < y+k*j < 8:
                    j+=1
                    legal_moves.append([x+i*j, y+k*j])
            
        if self.race == 'K':
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not i==j==0:
                        legal_moves.append([x+i, y+j])

        # Removing the moves outside the board
        temp = []
        for l in legal_moves:
            if(-1 < l[0] < 8 and -1 < l[1] < 8):
                temp.append(l)

        # Removing the moves that take the same color piece
        legal_moves = []
        for l in temp:
            if l in locations:
                index = locations.index(l)
                selected = board[index]
                if not board[index].color == self.color:
                    legal_moves.append(l)
            else:
                legal_moves.append(l)

        return legal_moves


br_pic = pygame.image.load('./images/b_rook.png')
bn_pic = pygame.image.load('./images/b_knight.png')
bb_pic = pygame.image.load('./images/b_bishop.png')
bq_pic = pygame.image.load('./images/b_queen.png')
bk_pic = pygame.image.load('./images/b_king.png')
bp_pic = pygame.image.load('./images/b_pawn.png')
wr_pic = pygame.image.load('./images/w_rook.png')
wn_pic = pygame.image.load('./images/w_knight.png')
wb_pic = pygame.image.load('./images/w_bishop.png')
wq_pic = pygame.image.load('./images/w_queen.png')
wk_pic = pygame.image.load('./images/w_king.png')
wp_pic = pygame.image.load('./images/w_pawn.png')


# Black: Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
# Black: pawn8x
# White: pawn 8x
# White: Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
pieces = [
Piece([0, 0], 0, 'R', br_pic), Piece([1, 0], 0, 'N', bn_pic), Piece([2, 0], 0, 'B', bb_pic), Piece([3, 0], 0, 'Q', bq_pic), Piece([4, 0], 0, 'K', bk_pic), Piece([5, 0], 0, 'B', bb_pic), Piece([6, 0], 0, 'N', bn_pic), Piece([7, 0], 0, 'R', br_pic), 
Piece([0, 1], 0, 'P', bp_pic), Piece([1, 1], 0, 'P', bp_pic), Piece([2, 1], 0, 'P', bp_pic), Piece([3, 1], 0, 'P', bp_pic), Piece([4, 1], 0, 'P', bp_pic), Piece([5, 1], 0, 'P', bp_pic), Piece([6, 1], 0, 'P', bp_pic), Piece([7, 1], 0, 'P', bp_pic),
Piece([0, 6], 1, 'P', wp_pic), Piece([1, 6], 1, 'P', wp_pic), Piece([2, 6], 1, 'P', wp_pic), Piece([3, 6], 1, 'P', wp_pic), Piece([4, 6], 1, 'P', wp_pic), Piece([5, 6], 1, 'P', wp_pic), Piece([6, 6], 1, 'P', wp_pic), Piece([7, 6], 1, 'P', wp_pic),
Piece([0, 7], 1, 'R', wr_pic), Piece([1, 7], 1, 'N', wn_pic), Piece([2, 7], 1, 'B', wb_pic), Piece([3, 7], 1, 'Q', wq_pic), Piece([4, 7], 1, 'K', wk_pic), Piece([5, 7], 1, 'B', wb_pic), Piece([6, 7], 1, 'N', wn_pic), Piece([7, 7], 1, 'R', wr_pic)
]