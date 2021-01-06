import pygame 
import time
import random

pygame.init()

# rgb color variables
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)

# display setup
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

# snake size
snakeBlock = 10

# snake food init
foodx = 0
foody = 0

clock = pygame.time.Clock()
frameRate = 15

fontStyle = pygame.font.SysFont(None, 30)
scoreFont = pygame.font.SysFont("comicsansms", 35)

# draws snake
def mySnake(snake_Block, snake_List):
    for i in snake_List:
        pygame.draw.rect(window, blue, [i[0], i[1], snake_Block, snake_Block]) # draws snake

# function to display a center aligned message in a given color
def message(msg, color):
    m = fontStyle.render(msg, True, color)
    msgWidth = m.get_rect().width
    msgHeight = m.get_rect().height
    window.blit(m, [window_width/2 - msgWidth/2, window_height/2])

def displayScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

def gameLoop():
    run = True
    gameClosed = False

    # snake position
    x = window_width/2
    y = window_height/2

    # snake speed in each direction
    xVel = 0
    yVel = 0

    #
    snakeList = []
    snakeLen = 1

    # random food postition
    foodx = round(random.randrange(0, window_width - snakeBlock) / 10) * 10
    foody = round(random.randrange(0, window_height - snakeBlock) / 10) * 10

    while run:   

        while gameClosed == True:
            window.fill(black)
            message("Game Over! Press Q-Quit or P-Play Again", white)
            displayScore(snakeLen - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        gameClosed = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClosed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    xVel = -snakeBlock
                    yVel = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    xVel = snakeBlock
                    yVel = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    yVel = -snakeBlock
                    xVel = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    yVel = snakeBlock
                    xVel = 0

        # stops game if snake hits wall
        if(x >= window_width or x < 0 or y > window_height or y < 0):
            gameClosed = True

        # keeps snake moving in one direction until a key is pressed
        x += xVel
        y += yVel

        window.fill(black)
        pygame.draw.rect(window, white, [foodx, foody, snakeBlock, snakeBlock]) # draws food

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        # deletes snake as it moves
        if len(snakeList) > snakeLen:
            del snakeList[0]

        # ends game if snake runs into itself
        for i in snakeList[:-1]:
            if i == snakeHead:
                gameClosed = True

        mySnake(snakeBlock, snakeList)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, (window_width - snakeBlock)) / 10) * 10
            foody = round(random.randrange(0, (window_height - snakeBlock)) / 10) * 10
            snakeLen += 1

        clock.tick(frameRate)

    pygame.quit()
    quit()

gameLoop()