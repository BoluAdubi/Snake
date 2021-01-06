import pygame 

pygame.init()

black = (0, 0, 0)
blue = (0, 0, 255)

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game by Bolu")

run = True

x = 300
y = 300

xVel = 0
yVel = 0


clock = pygame.time.Clock()

while run:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                xVel = -8
                yVel = 0
                print("left pressed")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                xVel = 8
                yVel = 0
                print("right pressed")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                yVel = -8
                xVel = 0
                print("up pressed")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                yVel = 8
                xVel = 0
                print("down pressed")

    x += xVel
    y += yVel

    window.fill(black)
    pygame.draw.rect(window, blue, [x, y, 20, 20])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()