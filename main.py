import pygame
import FiguresTetris as fg
import Colors as color
import RandomFigures as rf
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

#For the queue of pieces
random_figs = rf.RandomFigures()
QUEUE_SIZE = 4
queue = list(range(QUEUE_SIZE))
random_figs.initialize_queue(queue, QUEUE_SIZE)
print("Initial queue: ", queue)


#To save the frozen pieces
placed_figures = []

#The delay in the velocity of the block
movement_delay_left = 0
COUNTER_DELAY = 3
movement_delay_right = 0
movement_delay_down = 0

#The current block falling
INITIAL_X = GRID_X+(GRID_WIDTH/2) - SIZE_BLOCK
INITIAL_Y = GRID_Y
block = Block.Block(queue[0], INITIAL_X, INITIAL_Y, GRID_X, GRID_X+GRID_WIDTH, GRID_Y, GRID_Y+GRID_HEIGHT, SIZE_BLOCK)

#Variables for the delay in freezing the piece
START_FREEZE_TIME = 900
time_to_freeze = START_FREEZE_TIME
first_contat_ground_time = 0
aux_bool_freeze = True


'''
s j o i t  l
#Test block
pos = figureMannager.getPositions(block.type_, SIZE_BLOCK, block.pos_x, block.pos_y, 3)

for p in pos:
    #print(p)
    pygame.draw.rect(screen, color.YELLOW, p, 0)
    pygame.draw.rect(screen, color.WHITE, p, 1, 0)
'''


#The grid collection of lines to draw
grid = figureMannager.getPositionsMesh(SIZE_BLOCK, GRID_WIDTH, GRID_HEIGHT, GRID_X, GRID_Y)

while running:
    #Events
    for event in pygame.event.get():
        #Handling only one input of the up button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                block.setRotation(block.rotation+1)
                print(block.rotation)
        #To handle the exit of the game
        if event.type == pygame.QUIT:
            running = False
        
        #Updating the fall of the piece
        if event.type == pygame.USEREVENT:
            block.setPos_y(block.pos_y + SIZE_BLOCK)

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

    
    #Refresh the screen to move the blocks
    screen.fill(color.BLACK)
    
    #Drawing the mesh
    for p in grid:
        pygame.draw.line(screen, color.WHITE, p[0], p[1], 2)

    #Draws the figures that are already frozen
    for b in placed_figures:
        pos = figureMannager.getPositions(b.type_, SIZE_BLOCK, b.pos_x, b.pos_y, b.rotation)
        for p in pos:
            pygame.draw.rect(screen, b.color, p, 0)
            pygame.draw.rect(screen, color.WHITE, p, 1, 0)

    #The logic for freezing the piece when it tocuhes the ground after certain time
    if(block.in_ground and aux_bool_freeze):
        #print("It tocuhed the ground")
        first_contat_ground_time = pygame.time.get_ticks()
        aux_bool_freeze = False
    
    if(not block.in_ground):
        aux_bool_freeze = True
        

    if(block.in_ground and (not aux_bool_freeze) and pygame.time.get_ticks()>=first_contat_ground_time+time_to_freeze):
        print("It will freeze")
        b = block
        placed_figures.append(b)
        random_figs.generate_next_piece(queue, QUEUE_SIZE)
        block = Block.Block(queue[0], INITIAL_X, INITIAL_Y, GRID_X, GRID_X+GRID_WIDTH, GRID_Y, GRID_Y+GRID_HEIGHT, SIZE_BLOCK)
        #block.freezed = True
        aux_bool_freeze = True
                
    #Draws the figure in the actual position
    pos = figureMannager.getPositions(block.type_, SIZE_BLOCK, block.pos_x, block.pos_y, block.rotation)
    for p in pos:
        #print(p)
        pygame.draw.rect(screen, block.color, p, 0)
        pygame.draw.rect(screen, color.WHITE, p, 1, 0)
    

    #Updates the display
    pygame.display.update()
    
    clock.tick(30)

pygame.quit()