import pygame
import FiguresTetris as fg
import Colors as color
import Block


#Basic configuration of the window
WIDTH_SCREEN = 500
HEIGHT_SCREEN = 700
SIZE_BLOCK = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
screen.fill(color.WHITE)

#The title of the window
pygame.display.set_caption("Tetris with no sprites")

#The boolean to control the game loop
running = True

#To manage the figures
figureMannager = fg.FiguresTetris()

#For the timer and clock
pygame.time.set_timer(pygame.USEREVENT, 1000)
clock = pygame.time.Clock()

#Position of the grid
GRID_WIDTH = 10*SIZE_BLOCK
GRID_HEIGHT = 20*SIZE_BLOCK
GRID_X =160
GRID_Y =40

#For the physics and position of the game
movement_delay_left = 0
COUNTER_DELAY = 3
movement_delay_right = 0
movement_delay_down = 0

#The current block falling 
block = Block.Block("L", GRID_X+(GRID_WIDTH/2) - SIZE_BLOCK, GRID_Y, GRID_X+GRID_WIDTH, GRID_Y+GRID_HEIGHT, SIZE_BLOCK)

print("The max X is: ", block.max_pos_x)

while running:
    #Handling inputs
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        #print("Left pressed")
        movement_delay_left+=1
        if(movement_delay_left>=COUNTER_DELAY):
            block.setPos_x(block.pos_x - SIZE_BLOCK)
            movement_delay_left = 0
    elif keys[pygame.K_RIGHT]:
        #print("Right pressed")
        movement_delay_right+=1
        if(movement_delay_right>=COUNTER_DELAY):
            block.setPos_x(block.pos_x + SIZE_BLOCK)
            movement_delay_right = 0

    elif keys[pygame.K_DOWN]:
        #print("Right pressed")
        movement_delay_down+=1
        if(movement_delay_down>=COUNTER_DELAY):
            block.setPos_y(block.pos_y + SIZE_BLOCK)
            movement_delay_down = 0
    
    #Events
    for event in pygame.event.get():
        #To handle the exit of the game
        if event.type == pygame.QUIT:
            running = False
        
        #Updating the fall of the piece
        if event.type == pygame.USEREVENT:
            block.setPos_y(block.pos_y + SIZE_BLOCK)

    #Refresh the screen to move the blocks
    screen.fill(color.BLACK)

    #Drawing the mesh
    pos = figureMannager.getPositionsMesh(SIZE_BLOCK, GRID_WIDTH, GRID_HEIGHT, GRID_X, GRID_Y)
    for p in pos:
        pygame.draw.line(screen, color.WHITE, p[0], p[1], 2)
    
    #Draws the figure in the actual position
    pos = figureMannager.getPositions(block.type_, SIZE_BLOCK, block.pos_x, block.pos_y)
    for p in pos:
        #print(p)
        pygame.draw.rect(screen, color.YELLOW, p, 0)
        pygame.draw.rect(screen, color.WHITE, p, 1, 0)
    
    #Updates the display
    pygame.display.update()

    clock.tick(30)

pygame.quit()