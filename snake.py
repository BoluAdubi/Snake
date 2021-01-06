import pygame 
import time

pygame.init()

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)

# display setup
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

#snake position
x = window_width/2
y = window_height/2

snakeBlock = 20

# snake speed in each direction
xVel = 0
yVel = 0

clock = pygame.time.Clock()
frameRate = 30

fontStyle = pygame.font.SysFont(None, 50)

# function to display a center aligned message in a given color
def message(msg, color):
    m = fontStyle.render(msg, True, color)
    msgWidth = m.get_rect().width
    msgHeight = m.get_rect().height
    window.blit(m, [window_width/2 - msgWidth/2, window_height/2])

run = True
userEnd = False

while run and not userEnd:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            userEnd = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                xVel = -snakeBlock * 0.4
                yVel = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                xVel = snakeBlock * 0.4
                yVel = 0
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                yVel = -snakeBlock * 0.4
                xVel = 0
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                yVel = snakeBlock * 0.4
                xVel = 0

    # stops game if snake hits wall
    if(x >= window_width - snakeBlock or x < 0 or y > window_height - snakeBlock or y < 0):
        run = False

    # keeps snake moving in one direction until a key is pressed
    x += xVel
    y += yVel

    window.fill(black)
    pygame.draw.rect(window, blue, [x, y, snakeBlock, snakeBlock])

    pygame.display.update()

    clock.tick(frameRate)

if run == False:
    message("Game Over", red)
    pygame.display.update()
    time.sleep(2)
elif userEnd == True:
    message("Exiting...", red)
    pygame.display.update()
    time.sleep(2)

pygame.quit()
quit()