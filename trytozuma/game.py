import pygame
import zuma
import constant
import ball

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zuma")
run = True
frog = zuma.Zuma(300, 300, constant.dictColor['red'], constant.dictColor['red'])
init = True
snake = ball.Snake()
ball = zuma.ballThrow(frog.x, frog.y, frog.currentColorBall)
def draw():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600))
    ball.render(screen)
    frog.render(screen)
    snake.render(screen)
    pygame.display.update()


while run:
    if init:
        draw()
        init = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            ball = zuma.ballThrow(frog.x, frog.y, frog.currentColorBall)
            frog.throw(event.pos, ball)
            frog.nextBall()
            while 0 < ball.x < 600 and 0 < ball.y < 600:
                ball.x = ball.x + ball.vx
                ball.y = ball.y + ball.vy
                draw()
            pygame.time.delay(100)
    if keys[pygame.K_r]:
        frog.changeBall()
        draw()
        pygame.time.delay(100)
pygame.quit()