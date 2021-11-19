from pieces import *

# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 800])

# Variables
selected = -1
legal_moves = []
n_move = 1

# Run until the user asks to quit
running = True
while running:

    # Get mouse data
    mouse_pos = pygame.mouse.get_pos()
    mouse_down = pygame.mouse.get_pressed(num_buttons=3)[0]
    pos_on_board = [mouse_pos[0]//100, mouse_pos[1]//100]

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw board
    bgcolor = [(57, 255, 20), (181, 101, 29)]
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(screen, bgcolor[(x+y)%2], pygame.Rect(100*x, 100*y, 100, 100))

    # Selecting the piece to move with
    if mouse_down:
        # All of the pieces on the board
        locations = [i.position for i in pieces]
        if pos_on_board in locations:
            index = locations.index(pos_on_board)
            if pieces[index].color == n_move:
                selected = pieces[index]
        
        # Making a move
        if pos_on_board in legal_moves:
            if pos_on_board in locations:
                index = locations.index(pos_on_board)
                pieces.pop(index)
            selected.position = pos_on_board
            n_move = -n_move+1
            selected = -1
            legal_moves = []

    if not selected == -1:
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect(100*selected.position[0], 100*selected.position[1], 100, 100))
        legal_moves = selected.legalMoves(pieces)

    
    # Draw possible moves
    for i in legal_moves:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100*i[0], 100*i[1], 100, 100))

    # Draw pieces
    for p in pieces:
        screen.blit(p.pic, (p.position[0]*100, p.position[1]*100))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()