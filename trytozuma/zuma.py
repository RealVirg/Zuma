import random
import constant
import pygame
import math
import ball

class Zuma(object):
    def __init__(self, x, y, currentColorBall, nextColorBall):
        self.x = x
        self.y = y
        self.currentColorBall = currentColorBall
        self.nextColorBall = nextColorBall


    def nextBall(self):
        randomColor = constant.dictColor[constant.numberColor[random.randint(1, constant.COUNTCOLOR)]]
        self.currentColorBall = self.nextColorBall
        self.nextColorBall = randomColor


    def changeBall(self):
        self.currentColorBall, self.nextColorBall = self.nextColorBall, self.currentColorBall


    def render(self, screen):
        pygame.draw.circle(screen, self.currentColorBall, (self.x, self.y), 10)
        pygame.draw.circle(screen, self.nextColorBall, (10, 10), 10)


    def throw(self, pick, ball):
        ball.vx = round((pick[0] - ball.x) / 10)
        ball.vy = round((pick[1] - ball.y) / 10)


class ballThrow(ball.Ball):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.xv = 0
        self.yv = 0


    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)